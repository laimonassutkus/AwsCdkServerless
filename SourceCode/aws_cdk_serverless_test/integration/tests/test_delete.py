import random
import uuid

import requests

from aws_cdk_serverless_test.integration.infrastructure import Infrastructure


def test_ENDPOINT_delete_WITH_existing_entity_EXPECT_successfuly_deleted():
    url = Infrastructure.api_url()
    name = str(uuid.uuid4())

    response = requests.post(
        url=f'{url}/create',
        json={
            'name': name,
            'age': random.randrange(1, 10),
            'color': 'brown'
        }
    )

    assert response.status_code == 201

    response = requests.delete(
        url=f'{url}/delete',
        json={
            'name': name,
        }
    )

    assert response.status_code == 200
