from src.app.app_settings import AppSettings
from src.kafka.consumer.consumer import KafkaConsumer
from tests.kafka.testutils.consumer_callback import TestConsumerCallBack

if __name__ == '__main__':
    AppSettings()
    consumer = KafkaConsumer(bootstrap_servers=AppSettings.CREDENTIALS["messageBrokers"]["kafka"]["servers"],
                             group_id=AppSettings.APP_SETTINGS["messageBrokers"]["kafka"]["groupId"],
                             auto_offset_reset='earliest')
    topic = "sample-topic"
    callback = TestConsumerCallBack(topic)
    print('start test')
    consumer.subscribe([callback])
    consumer.consume()
    consumer.close()