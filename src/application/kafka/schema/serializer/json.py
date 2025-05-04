from typing import Callable, Any

from src.application.kafka.schema.schema_reg import SchemaRegClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from confluent_kafka.serialization import StringSerializer, MessageField, SerializationContext


class JsonSerializer:
    def __init__(self, schema_reg_client: SchemaRegClient, schema_str, to_dict_fun: Callable):
        self.__serializer = JSONSerializer(schema_str,
                                                  schema_reg_client.schema_registry,
                                                  to_dict=to_dict_fun)
        self.__key_serializer = StringSerializer()

    def __call__(self, topic, key, obj: Any):
        return self.__key_serializer(key), self.__serializer(obj, SerializationContext(topic, MessageField.VALUE))