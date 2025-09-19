import pytest
import allure
from src.clients.authors_client import AuthorsClient
from src.utils.debug import log_response, log_request_payload

client = AuthorsClient()

@allure.feature("Authors API")
@allure.story("Retrieve all authors")
def test_get_all_authors():
    response = client.get_all_authors()
    log_response(response, "GET /Authors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@allure.feature("Authors API")
@allure.story("Retrieve author by valid ID")
def test_get_author_by_valid_id():
    response = client.get_author_by_id(1)
    log_response(response, "GET /Authors/1")
    assert response.status_code == 200
    assert response.json()['id'] == 1

@allure.feature("Authors API")
@allure.story("Retrieve author by invalid ID")
def test_get_author_by_invalid_id():
    response = client.get_author_by_id(9999)
    log_response(response, "GET /Authors/9999")
    assert response.status_code == 404

@allure.feature("Authors API")
@allure.story("Create a new author")
def test_create_author():
    payload = {
        "id": 2001,
        "idBook": 1,
        "firstName": "Mickey",
        "lastName": "Mouse"
    }
    log_request_payload(payload)
    response = client.create_author(payload)
    log_response(response, "POST /Authors")
    assert response.status_code == 200
    assert response.json()['firstName'] == "Mickey"

@allure.feature("Authors API")
@allure.story("Create author with missing fields")
def test_create_author_missing_fields():
    payload = {"id": 2002}
    log_request_payload(payload)
    response = client.create_author(payload)
    log_response(response, "POST /Authors (missing fields)")
    assert response.status_code == 200
# Validate response matches payload (since we can't GET it later)
    response_data = response.json()
    for key in payload:
        assert response_data[key] == payload[key]


@allure.feature("Authors API")
@allure.story("Update existing author")
def test_update_author():
    payload = {
        "id": 1,
        "idBook": 1,
        "firstName": "Updated",
        "lastName": "Author"
    }
    log_request_payload(payload)
    response = client.update_author(1, payload)
    log_response(response, "PUT /Authors/1")
    assert response.status_code == 200
    # Validate response reflects updated data
    response_data = response.json()
    for key in payload:
        assert response_data[key] == payload[key]


@allure.feature("Authors API")
@allure.story("Update author with invalid ID")
def test_update_author_invalid_id():
    payload = {
        "id": 9999,
        "idBook": 1,
        "firstName": "Invalid",
        "lastName": "Author"
    }
    log_request_payload(payload)
    response = client.update_author(9999, payload)
    log_response(response, "PUT /Authors/9999")
    assert response.status_code == 200
    # Validate response reflects updated data
    response_data = response.json()
    for key in payload:
        assert response_data[key] == payload[key]


@allure.feature("Authors API")
@allure.story("Delete existing author")
def test_delete_author():
    response = client.delete_author(2001)
    log_response(response, "DELETE /Authors/2001")
    assert response.status_code == 200

@allure.feature("Authors API")
@allure.story("Delete author with invalid ID")
def test_delete_author_invalid_id():
    response = client.delete_author(9999)
    log_response(response, "DELETE /Authors/9999")
    assert response.status_code == 200

@allure.feature("Authors API")
@allure.story("Create duplicate author")
def test_create_duplicate_author():
    payload = {
        "id": 2003,
        "idBook": 1,
        "firstName": "Duplicate",
        "lastName": "Author"
    }
    log_request_payload(payload)
    response1 = client.create_author(payload)
    log_response(response1, "POST /Authors (first attempt)")
    assert response1.status_code == 200

    response2 = client.create_author(payload)
    log_response(response2, "POST /Authors (second attempt)")
    # If API enforces uniqueness, expect 400; otherwise, document behavior
    assert response2.status_code in [200, 400]
