import json

from aws_cdk_serverless_layer.cat_model import CatModel


def handler(event, context):
    print(f'Received an event: {json.dumps(event)}.')

    json_body = json.loads(event['body'])
    print(f'Request body: {json_body}.')

    name = json_body['name']
    age = json_body['age']
    color = json_body['color']

    cat = CatModel()
    cat.name = name
    cat.age = age
    cat.color = color
    cat.save()

    return dict(
        statusCode=201,
        isBase64Encoded=False,
    )
