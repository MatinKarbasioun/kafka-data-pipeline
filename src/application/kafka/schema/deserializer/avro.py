from typing import Callable, Any

from confluent_kafka.schema_registry.avro import AvroDeserializer as _avroDeserializer
from confluent_kafka.serialization import MessageField, SerializationContext
from confluent_kafka import Message

from src.application.kafka.schema.schema_reg import SchemaRegClient


class AvroDeserializer:
    def __init__(self, schema_reg_client: SchemaRegClient, schema_str, from_dict_func: Callable):
        self.__deserializer = _avroDeserializer(schema_registry_client=schema_reg_client.schema_registry,
                                                schema_str=schema_str,
                                                from_dict=from_dict_func)

    def __call__(self, event: Message):
        return self.__deserializer(event.value(None), SerializationContext(event.topic(), MessageField.VALUE))