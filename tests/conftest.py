from pytest import fixture
from starlette.config import environ
from starlette.testclient import TestClient
from city_details.db.mongodb import get_database
from city_details.core.config import database_name, cities_collection_name


@fixture(scope="session")
def test_city():
    return {
        "count": 1,
        "cities": [
            {
                "city": "Pune",
                "city_ascii": "Pune",
                "lat": 18.5196,
                "lng": 73.8553,
                "country": "India",
                "iso2": "IN",
                "iso3": "IND",
                "admin_name": "Maharashtra",
                "capital": "",
                "population": 7764000,
                "id": 1356081074
            }
        ]
    }


@fixture(scope="session")
def test_client(test_city):
    from city_details import app
    with TestClient(app) as test_client:
        yield test_client

    import asyncio
    db = asyncio.run(get_database())
    db[database_name][cities_collection_name].find_one({"city": test_city["cities"][0]["city"]})


environ['TESTING'] = 'TRUE'