import json

from aws_cdk_serverless_layer.cat_model import CatModel


def handler(event, context):
    print(f'Received an event: {json.dumps(event)}.')

    json_body = json.loads(event['body'])
    print(f'Request body: {json_body}.')

    name = json_body['name']

    cat = CatModel()
    cat.name = name
    cat.delete()

    return dict(
        statusCode=200,
        isBase64Encoded=False,
    )
