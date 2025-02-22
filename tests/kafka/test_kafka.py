import pytest
from src.app.app_settings import AppSettings
from src.kafka.consumer.consumer import KafkaConsumer
from src.kafka.producer.producer import KafkaProducer
from tests.kafka.testutils.consumer_callback import TestConsumerCallBack
from tests.kafka.testutils.producer_callback import TestProducerCallBack


@pytest.fixture(scope="module")
def topic():
    sample_topic = "sample-topic"
    return sample_topic

@pytest.fixture(scope="module")
def create_producer():
    AppSettings()
    producer = KafkaProducer({"bootstrap.servers": AppSettings.CREDENTIALS["messageBrokers"]["kafka"]["servers"]})
    return producer

@pytest.fixture(scope="module")
def create_consumer():
    AppSettings()
    consumer = KafkaConsumer(bootstrap_servers=AppSettings.CREDENTIALS["messageBrokers"]["kafka"]["servers"],
                             group_id=AppSettings.APP_SETTINGS["messageBrokers"]["kafka"]["groupId"],
                             auto_offset_reset='earliest')
    return consumer

def test_produce_data_should_return_true_result(create_producer: KafkaProducer, topic: str):
    keys = ['Amy', 'Brenda', 'Cindy', 'Derrick', 'Elaine', 'Fred']
    callback = TestProducerCallBack()
    [create_producer.sync_produce(topic=topic, value=f"hello {key}!", key=key,
                                  callback=callback) for key in keys]
    create_producer.close()

    assert callback.flag == True

def test_consume_data_should_return_true_flag_when_received_event(create_consumer: KafkaConsumer, topic: str):
    callback = TestConsumerCallBack(topic)
    print('start test')
    consumer = create_consumer
    consumer.subscribe([callback])
    consumer.consume()
    consumer.close()

    assert callback.flag == True
