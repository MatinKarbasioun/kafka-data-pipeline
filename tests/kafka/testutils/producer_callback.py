from src.kafka.producer.IKafkaProducerCallback import IKafkaProducerCallback


class TestProducerCallBack(IKafkaProducerCallback):
    def __init__(self):
        self.__flag = False

    def on_receive(self, err, event):

        if err:
            print(f'Produce to topic {event.topic()} failed for event: {event.key()}')
            self.__flag = False

        else:
            self.__flag = True
            val = event.value().decode('UTF-8')
            print(f'{val} sent to partition {event.partition()}.')

    @property
    def flag(self):
        return self.__flag

