from typing import Callable, Any

from src.application.kafka.schema.schema_reg import SchemaRegClient
from confluent_kafka.schema_registry.json_schema import JSONDeserializer, SerializationContext
from confluent_kafka.serialization import MessageField, StringDeserializer
from confluent_kafka import Message


class JsonSerializer:
    def __init__(self, schema_str, from_dict_func: Callable):
        self.__deserializer = JSONDeserializer(schema_str, from_dict=from_dict_func)

    def __call__(self, event: Message):
        return self.__deserializer(event.value(None), SerializationContext(event.topic(), MessageField.VALUE))