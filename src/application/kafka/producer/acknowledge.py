import asyncio
import logging

from confluent_kafka import KafkaException

from src.application.kafka.producer.IKafkaProducerCallback import IKafkaProducerCallback

logger = logging.getLogger(__name__)


class AsyncAcknowledge(IKafkaProducerCallback):
    def __init__(self, topic, loop):
        self.__topic = topic
        self.__loop = loop or asyncio.get_event_loop()

    def on_receive(self, err, event):
        result = self.__loop.create_future()

        if err:
            logger.error(f'Produce to topic {event.topic()} failed for event: {event.key()}')
            self.__loop.call_soon_threadsafe(result.set_exception, KafkaException(err))

        else:
            self.__loop.call_soon_threadsafe(result.set_result, event)
            val = event.value().decode('UTF-8')
            logger.info(f'{val} sent to partition {event.partition()}.')

    @property
    def topic(self):
        return self.__topic