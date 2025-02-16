import pytest
from src.app.app_settings import AppSettings
from src.kafka.producer.producer import KafkaProducer
from tests.kafka.testutils.callback import TestProducerCallBack


@pytest.fixture(scope="module")
def create_producer():
    AppSettings()
    producer = KafkaProducer({"bootstrap.servers": AppSettings.CREDENTIALS["messageBrokers"]["kafka"]["servers"]})
    return producer

def test_produce_data_should_return_true_result(create_producer: KafkaProducer):
    sample_topic = "sample-topic"
    keys = ['Amy', 'Brenda', 'Cindy', 'Derrick', 'Elaine', 'Fred']
    callback = TestProducerCallBack(False)
    [create_producer.sync_produce(topic=sample_topic, value=f"hello {key}!", key=key,
                                  callback=callback) for key in keys]
    create_producer.close()

    assert callback.flag == True
