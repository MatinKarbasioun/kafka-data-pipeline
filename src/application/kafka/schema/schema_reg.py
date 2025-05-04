# provide access to schema registry

"""
Json Serializer
Protobuf Serializer
Avro Serializer

schema should:
1- versioned schema repo
2- safe schema evolution
3- resilient schema evolution
4- Enhanced data integrity
5- Reduce storage and computation
6- Discover data
7- Cost-efficient ecosystem

"""

from confluent_kafka.schema_registry import SchemaRegistryClient


class SchemaRegClient:
    def __init__(self, schema_registry_url, authentication, schema_registry_topic):
        self.__sc = SchemaRegistryClient(conf={
            "url": schema_registry_url,
            "basic.auth.user.info": authentication,
        })

    @property
    def schema_registry(self) -> SchemaRegistryClient:
        return self.__sc
