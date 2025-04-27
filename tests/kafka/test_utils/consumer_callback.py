from confluent_kafka import Message

from src.application.kafka.consumer.consumer_callback import IKafkaConsumerCallback


class TestConsumerCallBack(IKafkaConsumerCallback):
    def __init__(self, sample_topic: str):
        self.__topic = sample_topic
        self.__flag = False

    def on_receive(self, msg: Message):
        key = msg.key().decode('utf-8')
        value = msg.value().decode('utf-8')
        print(f'Received {key}: {value} in topic {self.__topic}')
        self.__flag = True

    @property
    def topic(self) -> str:
        return self.__topic

    @property
    def flag(self) -> bool:
        return self.__flag
