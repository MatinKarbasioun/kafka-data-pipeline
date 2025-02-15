import asyncio
from threading import Thread
from typing import Type

import confluent_kafka
from confluent_kafka import KafkaException

from src.kafka.ICallback import ICallback

"""
Producer responsible to:
1- Partition assignment
2- Batching events for improved throughput
3- Compression
4- Retries
5- Response callbacks
6- Transaction handling
"""
class AIOKafkaProducer:
    def __init__(self, configs, loop=None):
        self._loop = loop or asyncio.get_event_loop()
        self._producer = confluent_kafka.Producer(configs)
        self._cancelled = False
        self._poll_thread = Thread(target=self._poll_loop)
        self._poll_thread.start()

    def _poll_loop(self):
        while not self._cancelled:
            self._producer.poll(0.1)

    def close(self):
        self._cancelled = True
        self._poll_thread.join()

    def produce(self,
                topic,
                value: str|bytes|None = None,
                keys:str|bytes|None=None,
                partitions:int|None=None,
                on_delivery: Type[ICallback] | None = None,
                timestamps:int|None=None,
                headers:dict|None=None):
        result = self._loop.create_future()


        self._producer.produce(topic, value, on_delivery=ack)
        return result