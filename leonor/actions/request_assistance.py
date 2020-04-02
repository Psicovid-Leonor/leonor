import json


class RequestAssistance:
    def __init__(self, notifier, encoding_service):
        self._notifier = notifier
        self.encoding_service = encoding_service

    def execute(self, event):
        input_data = json.loads(event['body'])
        encoded_request = self.encoding_service.encode(input_data)
        hour = input_data['hour']

        self._notifier.notify(
            message=f'NUEVA CITA:\nHora: {hour}\nPinche en el siguiente link para aceptar:\n'
                    f'http://psicovid.org/cita_{encoded_request}'
        )
