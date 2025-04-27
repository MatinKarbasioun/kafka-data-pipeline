"""
Convert data into bytes to stored in kafka topics
Accepted data: string, int, double (string serializer, int serializer, double serializer)
"""
from confluent_kafka.schema_registry.json_schema import JsonSchema

class Serializer:
    pass
