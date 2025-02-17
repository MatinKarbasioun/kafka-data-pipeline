import logging

logger = logging.getLogger(__name__)


class KafkaAssign:

    @classmethod
    def on_assign(cls, consumer, topic_partitions):
        for tp in topic_partitions:
            logger.info('kafka consumer assign on topic: {}, partition {}, offset {}'.format(tp.topic,
                                                                                             tp.partition,
                                                                                             tp.offset))
