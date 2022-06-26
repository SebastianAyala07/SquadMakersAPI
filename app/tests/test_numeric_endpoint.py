import os
import pytest
from app import create_app

@pytest.fixture(scope="module")
def client_testing():
    app_instance = create_app(
        os.getenv("APP_SETTINGS_MODULE")
    )
    with app_instance.test_client() as testing_client:
        with app_instance.app_context():
            yield testing_client

def test_numeric_numbers_endpoint(client_testing):
    params = {
        "numbers": [5, 4, 3]
    }
    response = client_testing.get("/num", query_string=params)
    response = response.get_json()
    assert response["value"] == 60

def test_numeric_number_endpoint(client_testing):
    params = {
        "number": 5
    }
    response = client_testing.get("/num", query_string=params)
    response = response.get_json()
    assert response["value"] == 6
