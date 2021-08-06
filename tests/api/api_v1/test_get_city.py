def test_get_city(test_client, test_city):
    response = test_client.get("/cities?city=Pune")
    assert response.status_code == 200
    assert response.json()["count"] == 1
    assert response.json()["cities"][0]["city"] == test_city["cities"][0]["city"]

