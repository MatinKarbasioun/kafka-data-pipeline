from typing import Any

from pykka import ThreadingActor


class Writer(ThreadingActor):
    super().__init__()


    def on_receive(self, message: Any) -> Any:
        pass

    def write(self):
        pass