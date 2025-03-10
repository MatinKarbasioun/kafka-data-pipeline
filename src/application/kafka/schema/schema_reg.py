# provide access to schema registry

"""
Json Serializer
Protobuf Serializer
Avro Serializer
"""

from confluent_kafka.schema_registry import SchemaRegistryClient


class SchemaRegistry:
    def __init__(self, schema_registry_url, authentication, schema_registry_topic):
        self.__sc = SchemaRegistryClient(conf={
            "url": schema_registry_url,
            "basic.auth.user.info": authentication,
        })

    @property
    def schema_registry(self):
        return self.__sc
