class ICallback:
    def __init__(self, loop):
        self.__loop = loop

    def on_receive(self, err, msg):
        raise NotImplementedError
