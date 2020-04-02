from leonor.actions.request_assistance import RequestAssistance
from leonor.domain.notifier import Notifier
from leonor.domain.encoding_service import EncodingService
from leonor.infrastructure.telegram_notifier import TelegramNotifier


class Factory:
    @staticmethod
    def request_assistance():
        notifier = Notifier(channel=TelegramNotifier())
        return RequestAssistance(notifier=notifier, encoding_service=EncodingService())
