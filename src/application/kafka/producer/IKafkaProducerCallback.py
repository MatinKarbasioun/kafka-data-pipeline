from abc import abstractmethod


class IKafkaProducerCallback:

    @abstractmethod
    def on_receive(self, err, event):
        raise NotImplementedError
