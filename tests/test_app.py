

# "Real unit test": all elements outside the function is mocked
def test_apiTemperature_return200(mocker, client):
    get_last_temp_mock = mocker.patch(
        "ferment_pi.main.get_last_temperature")

    get_last_temp_mock.return_value = {"temperature": 10}

    response = client.get("/api/temperature")
    assert response.status_code == 200


# "Social unit test": we are using different "units" together,
# mocking only the Database
def test_apiTemperature_returnDataFromDb(mock_get_session, client):
    response = client.get("/api/temperature")
    assert response.status_code == 200
    resp_content = response.json()
    assert resp_content['data']['humidity'] == "33"
    assert resp_content['data']['temperature'] == "20"
    assert resp_content['data']['date'] == "2022-03-08T17:45:12.586682"
