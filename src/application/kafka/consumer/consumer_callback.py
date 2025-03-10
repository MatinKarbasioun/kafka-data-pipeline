from confluent_kafka import Message


class IKafkaConsumerCallback:

    """
    msg has these methods:
    1- error() --> kafka error or None
    2- key() --> str, bytes, or None
    3- value() --> str, bytes, or None
    4- headers() --> list of tuples (key, value)
    5- timestamp() --> tuple of timestamp type (TIMESTAMP_CREATE_TIME) or (TIMESTAMP_LOG_APPEND_TIME) and value
    6- topic() --> str, None
    7- partition() --> int, None
    8- offset() --> int, None

    """
    def on_receive(self, msg: Message):
        raise NotImplementedError

    @property
    def topic(self) -> str:
        raise NotImplementedError
