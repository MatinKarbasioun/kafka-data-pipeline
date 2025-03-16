from typing import Any

from pykka import ThreadingActor


class Publisher(ThreadingActor):
    super().__init__()

    def on_receive(self, message: Any) -> Any:
        pass


    def broadcast(self):
        pass
