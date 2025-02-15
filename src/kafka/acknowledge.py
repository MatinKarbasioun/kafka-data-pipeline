class Acknowledge:
    def __init__(self, loop):
        pass

    def ack(err, msg):
        if err:
            self._loop.call_soon_threadsafe(
                result.set_exception, KafkaException(err))
        else:
            self._loop.call_soon_threadsafe(
                result.set_result, msg)