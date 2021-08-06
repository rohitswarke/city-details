from city_details.api.api_v1.routes.health_checker_router import HealthResponse
from mock import patch
import pytest
import pydantic


def test_health_checker(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
    # print(f'Response: {response.json()}')
    assert response.json()["configurations"][0]["database_name"] == "CITY_DETAILS"
    assert response.json()["information"] == "All routers are up and running"


def test_unhealty_checker(test_client):
    with patch('city_details.api.api_v1.routes.health_checker_router.HealthResponse') as mock:
        instance = mock.return_value
        instance.is_healthy = False
        print(f'instance: {instance}')
        with pytest.raises(pydantic.error_wrappers.ValidationError) as e:
            response = test_client.get("/health")

