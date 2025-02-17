import logging

logger = logging.getLogger(__name__)


class KafkaPartitioning:

    @classmethod
    def on_assign(cls, consumer, topic_partitions):
        for tp in topic_partitions:
            logger.info('kafka consumer assign on topic: {}, partition {}, offset {}'.format(tp.topic,
                                                                                             tp.partition,
                                                                                             tp.offset))

    @classmethod
    def on_revoke(cls, consumer, topic_partitions):
        for tp in topic_partitions:
            logger.info('kafka consumer revoke on topic: {}, partition {}, offset {}'.format(tp.topic,
                                                                                             tp.partition,
                                                                                             tp.offset))

    @classmethod
    def on_lost(cls, consumer, topic_partitions):
        for tp in topic_partitions:
            logger.info('kafka consumer lost partition on topic: {}, partition {}, offset {}'.format(tp.topic,
                                                                                             tp.partition,
                                                                                             tp.offset))

