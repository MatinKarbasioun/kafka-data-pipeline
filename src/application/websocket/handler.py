from abc import ABC, abstractmethod

from websockets import ServerConnection


class IWebSocketHandler(ABC):

    @abstractmethod
    def on_connection(self, websocket: ServerConnection):
        raise NotImplementedError
