import json

from aws_cdk_serverless_layer.cat_model import CatModel


def handler(event, context):
    print(f'Received an event: {json.dumps(event)}.')

    json_body = json.loads(event['body'])
    print(f'Request body: {json_body}.')

    name = json_body['name']
    age = json_body.get('age')
    color = json_body.get('color')

    update_actions = []

    if age: update_actions.append(CatModel.age.set(age))
    if color: update_actions.append(CatModel.color.set(color))

    cat = CatModel()
    cat.name = name
    cat.update(update_actions)

    return dict(
        statusCode=200,
        isBase64Encoded=False,
    )
