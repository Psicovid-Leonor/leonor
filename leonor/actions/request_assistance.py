import json


class RequestAssistance:
    def __init__(self, notifier):
        self._notifier = notifier

    def execute(self, event):
        input_data = json.loads(event['body'])
        hospital = input_data['hospital']
        phone_number = input_data['phone_number']
        hour = input_data['hour']

        self._notifier.notify(
            message=f'NUEVA CITA: \nHospital {hospital} \nContacto: {phone_number} \nHora: {hour}'
        )
