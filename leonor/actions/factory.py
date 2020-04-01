from leonor.actions.request_assistance import RequestAssistance
from leonor.domain.notifier import Notifier
from leonor.infrastructure.telegram_notifier import TelegramNotifier


class Factory:
    @staticmethod
    def request_assistance():
        notifier = Notifier(channel=TelegramNotifier())
        return RequestAssistance(notifier=notifier)
