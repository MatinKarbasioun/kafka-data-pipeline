import logging
from threading import Thread
from typing import TypeVar

import confluent_kafka

from src.application.kafka.producer.IKafkaProducerCallback import IKafkaProducerCallback

"""
Producer responsible to:
1- Partition assignment
2- Batching events for improved throughput
3- Compression
4- Retries
5- Response callbacks
6- Transaction handling
"""

logger = logging.getLogger(__name__)

CallBackType = TypeVar("CallBackType", bound=IKafkaProducerCallback)


class KafkaProducer:
    def __init__(self, configs):

        self._producer = confluent_kafka.Producer(configs)
        self._cancelled = False
        self._poll_thread = Thread(target=self._poll_loop)
        self._poll_thread.start()
        self.__timeout = 1

    def _poll_loop(self):
        while not self._cancelled:
            self._producer.poll(0.1)

    def close(self):
        self._cancelled = True
        self._poll_thread.join()

    def async_produce(self,
                      topic,
                      value: str | bytes | None = None,
                      key: str | bytes | None = None,
                      partition:int=-1,
                      callback: CallBackType | None = None,
                      timestamp:int=0,
                      headers: dict | None = None):
        self._producer.produce(topic, value, key=key, on_delivery=callback, partition=partition, timestamp=timestamp,
                               headers=headers)

    def sync_produce(self,
                     topic,
                     value: str|bytes|None = None,
                     key:str|bytes|None=None,
                     partition:int=-1,
                     callback: CallBackType | None = None,
                     timestamp:int=0,
                     headers:dict|None=None):

        if callback:
            callback = callback.on_receive

        self._producer.produce(topic, value, key=key, on_delivery=callback, partition=partition, timestamp=timestamp,
                               headers=headers)
        self._producer.flush()

    def init_transaction(self): # initialize transaction handling for this producer instance (prepare instance to participate to one or more transactions)
        self._producer.init_transactions(self.__timeout)

    def begin_transaction(self): # begin new transaction
        self._producer.begin_transaction()

    def commit_transaction(self): # Flush any active produce requests and mark transaction as committed | after be successful transaction on delivery we commit transactions and mark all the transactions as a successful
        self._producer.commit_transaction(self.__timeout)

    def abort_transaction(self): # Purge all produce requests in this transaction and mark transaction as aborted | if sometime something going wrong in our transactions we need abort it
        self._producer.abort_transaction(self.__timeout)

    def send_offsets_to_transaction(self, offsets, group_metadata): # when we use both producing and consuming events together, we used it to communicate with consumer group (this use to participate producer and consumer in sync together)
        self._producer.send_offsets_to_transaction(offsets, group_metadata, self.__timeout)