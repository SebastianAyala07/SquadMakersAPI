import os
import pytest
from app import create_app

@pytest.fixture
def client_testing():
    app_instance = create_app(
        os.getenv("APP_SETTINGS_MODULE")
    )
    with app_instance.test_client() as testing_client:
        with app_instance.app_context():
            yield testing_client

def test_numeric_numbers_endpoint(client_testing):
    params = {
        "numbers": "3,4,5"
    }
    response = client_testing.get("/num/", query_string=params)
    response = response.get_json()
    assert response["value"] == 60

def test_numeric_number_endpoint(client_testing):
    params = {
        "number": 5
    }
    response = client_testing.get("/num/", query_string=params)
    response = response.get_json()
    assert response["value"] == 6

def test_joke_endpoit_chuck(client_testing):
    response = client_testing.get("/joke/dad")
    assert response.status_code == 200
    response = response.get_json()
    print(response)
    assert isinstance(response["joke"], str)

def test_joke_endpoit_dad(client_testing):
    response = client_testing.get("/joke/chuck")
    assert response.status_code == 200
    response = response.get_json()
    print(response)
    assert isinstance(response["joke"], str)