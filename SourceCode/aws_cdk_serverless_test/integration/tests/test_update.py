import random
import uuid

import requests

from aws_cdk_serverless_test.integration.infrastructure import Infrastructure


def test_ENDPOINT_update_WITH_existing_entity_EXPECT_successfuly_update():
    url = Infrastructure.api_url()
    name = str(uuid.uuid4())
    age = random.randrange(1, 10)
    color = 'brown'

    response = requests.post(
        url=f'{url}/create',
        json={
            'name': name,
            'age': age,
            'color': color
        }
    )

    assert response.status_code == 201

    response = requests.get(
        url=f'{url}/read',
        params={
            'name': name,
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data['name'] == name
    assert data['age'] == age
    assert data['color'] == color

    response = requests.put(
        url=f'{url}/update',
        json={
            'name': name,
            'color': 'red'
        }
    )

    assert response.status_code == 200

    response = requests.get(
        url=f'{url}/read',
        params={
            'name': name,
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data['name'] == name
    assert data['age'] == age
    assert data['color'] == 'red'
