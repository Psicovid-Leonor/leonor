class Notifier:
    def __init__(self, channel):
        self._channel = channel

    def notify(self, message):
        self._channel.notify(message)
