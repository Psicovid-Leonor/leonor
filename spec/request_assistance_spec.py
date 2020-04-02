from mamba import description, context, it
from doublex import Spy, Stub, ANY_ARG
from expects import expect
from doublex_expects import have_been_called_with

from leonor.actions.request_assistance import RequestAssistance


def a_requested_event():
    return {
        "body": "{\"hospital\": \"an_hospital\", \"phone_number\": \"a_phone_number\", \"hour\": \"an_hour\"}"
    }


with description('RequestAssistance', 'unit'):
    with context('When a user request assistance'):
        with it('should send a notification with the encoded request data'):
            notifier_spy = Spy()
            with Stub() as encoding_service_stub:
                encoding_service_stub.encode(ANY_ARG).returns('an_encoded_string')
            action = RequestAssistance(notifier=notifier_spy, encoding_service=encoding_service_stub)

            action.execute(event=a_requested_event())

            expected_message = 'NUEVA CITA:\nHora: an_hour\nPinche en el siguiente link para aceptar:\n' \
                               'http://psicovid.org/cita_an_encoded_string'
            expect(notifier_spy.notify).to(have_been_called_with(message=expected_message))
