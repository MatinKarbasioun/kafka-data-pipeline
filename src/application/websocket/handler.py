from abc import ABC, abstractmethod


class IWebSocketHandler(ABC):

    @abstractmethod
    def on_receive(self, message):
        raise NotImplementedError
