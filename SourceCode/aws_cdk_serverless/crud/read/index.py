import json

from aws_cdk_serverless_layer.cat_model import CatModel


def handler(event, context):
    print(f'Received an event: {json.dumps(event)}.')

    query_string_parameters = event['queryStringParameters']
    name = query_string_parameters['name']

    cat = CatModel.get(name)

    return dict(
        statusCode=200,
        isBase64Encoded=False,
        headers={
            'Content-Type': 'application/json'
        },
        body=json.dumps(
            {
                'name': cat.name,
                'age': cat.age,
                'color': cat.color,
            }
        )
    )
