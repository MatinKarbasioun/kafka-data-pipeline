from typing import Callable, Any

from src.application.kafka.schema.schema_reg import SchemaRegClient
from confluent_kafka.schema_registry.protobuf import ProtobufSerializer
from confluent_kafka.serialization import StringSerializer, MessageField, SerializationContext


class ProtoSerializer:
    def __init__(self, schema_reg_client: SchemaRegClient, schema_str, pb2_obj: Callable):
        self.__serializer = ProtobufSerializer(pb2_obj,
                                               schema_reg_client.schema_registry,
                                           {'use.deprecated.format': False}) # Prevent crash with the older code
        self.__key_serializer = StringSerializer()

    def __call__(self, topic, key, obj: Any):
        return self.__key_serializer(key), self.__serializer(obj, SerializationContext(topic, MessageField.VALUE))