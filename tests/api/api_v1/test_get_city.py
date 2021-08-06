def test_get_city(test_client, test_input):
    response = test_client.get("/api/cities", city='Tokyo')
    assert response.status_code == 201
    assert response.json()["count"] == 1
