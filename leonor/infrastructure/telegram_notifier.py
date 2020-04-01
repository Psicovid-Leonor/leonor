import os
from telegram import Bot

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['CHAT_ID']


class TelegramNotifier:
    def __init__(self):
        self._bot = Bot(token=TELEGRAM_TOKEN)

    def notify(self, message):
        self._bot.sendMessage(
            chat_id=CHAT_ID,
            text=message
        )
