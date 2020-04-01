from leonor.actions.factory import Factory as ActionsFactory


def request_assistance(event, context):
    ActionsFactory.request_assistance().execute(event)

    response = {
        'statusCode': 200,
        'body': 'The appointment was successfully requested'
    }
    return response
