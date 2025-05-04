from typing import Callable, Any

from confluent_kafka.schema_registry.protobuf import ProtobufDeserializer as _protoDeserializer
from confluent_kafka.serialization import MessageField, SerializationContext
from confluent_kafka import Message


class ProtobufDeserializer:
    def __init__(self, schema_str):
        self.__deserializer = _protoDeserializer(schema_str, {'use.deprecated.format': False})

    def __call__(self, event: Message):
        return self.__deserializer(event.value(None), SerializationContext(event.topic(), MessageField.VALUE))