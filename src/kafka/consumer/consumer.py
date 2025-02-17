"""
Consumer responsible for:
1- Reads events from kafka topic
2- Keeps track of completed events (by updating the committed offset, done by us in our app, by configura by us we
ensure to the process is completed first)
3- Scales horizontally with Consumer Groups (Consumer can read events from all partitions of a topic or we can run
multiple consumers in parallel and they participate as a consumer group which will balance workload among all running
instances (event in a one partition cannot be consumed by more than one instance of the same consumer application, so
if we want to have multiple instances, we require multiple partitions)
Partitions are a key unit of scale in Kafka (the number of partitions is important)
The isolation level is important, by set our isolation to read committed offset, a consumer will not read any events
that are part of an open or boarded transaction.
"""
import logging

from confluent_kafka import Consumer, Message, KafkaException

from src.kafka.consumer.partitioning import KafkaPartitioning
from src.kafka.consumer.consumer_callback import IKafkaConsumerCallback

logger = logging.getLogger(__name__)

"""
 1- group.id: (str) Uniquely identifies this application so that additional instances are included in a consumer group
 2- auto.offset.reset: (latest) or (earliest) Determines offset to begin consuming at if no valid stored offset is 
 available, start from the latest event (another option is start from the beginning of the topic), once application 
 are running and offsets are begin commited, the commited offsets will be used to determine the starting point,
 however the committed offset is no longer valid, the auto.offset.reset comes to play and use again 
 3- enable.auto.commit: (true) if true, periodically commit offsets in the background (recommendation: as a tradeoff 
 set the enable.auto.commit to false and to commit offsets intentionally in our code.
 4- isolation.level: (read_committed): used in transactional processing. (read_uncommitted, read_commited)
 determines whenever our consumer reading events that were produced as part of a transaction. If this value sets to
 read_uncommitted, our consumer reads all events, also those are aborted or uncompleted transactions.
 
"""

class KafkaConsumer:
    def __init__(self, bootstrap_servers: str,
                 group_id: str,
                 auto_offset_reset: str = 'latest',
                 auto_commit: bool = False,
                 isolation_level: str = 'read_committed'):
        self.__assigned_callbacks = {}
        self.__consumer = Consumer({"bootstrap.servers": bootstrap_servers,
                                   "group.id":group_id,
                                   "auto.offset.reset":auto_offset_reset,
                                   "enable.auto.commit":auto_commit,
                                   "isolation.level":isolation_level})

    def subscribe(self, callbacks: list[IKafkaConsumerCallback], on_assign=KafkaPartitioning.on_assign,
                  on_revoke=KafkaPartitioning.on_revoke, on_lost=KafkaPartitioning.on_lost):
        [self.__add_subscriber(callback) for callback in callbacks]
        self.__consumer.subscribe(list(self.__assigned_callbacks.keys()),
                                  on_assign=on_assign,
                                  on_revoke=on_revoke,
                                  on_lost=on_lost)

    def __add_subscriber(self, callback: IKafkaConsumerCallback):
        self.__assigned_callbacks.update({callback.topic: callback})

    def __call_callbacks(self, event: Message):
        try:
            self.__assigned_callbacks.get(event.topic()).on_receive(event)

        except Exception as e:
            logger.error(f'There is an exception while processing callbacks in kafka consumer with {e} error')

    def consume(self):
        while True:
            event = self.__consumer.poll(timeout=0.01)

            if event is None:
                continue

            if event.error():
                logger.error(f"consumer event has error value {event.error()}")
                raise KafkaException(event.error())

            else:
                self.__call_callbacks(event)
                self.__consumer.commit(event)
