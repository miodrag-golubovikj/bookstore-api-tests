import pytest
import allure
from src.clients.authors_client import AuthorsClient

client = AuthorsClient()

@allure.feature("Authors API")
@allure.story("Retrieve all authors")
def test_get_all_authors():
    with allure.step("Send GET request to fetch all authors"):
        response = client.get_all_authors()
    with allure.step("Validate response"):
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@allure.feature("Authors API")
@allure.story("Retrieve author by valid ID")
def test_get_author_by_valid_id():
    response = client.get_author_by_id(1)
    assert response.status_code == 200
    assert response.json()['id'] == 1

@allure.feature("Authors API")
@allure.story("Retrieve author by invalid ID")
def test_get_author_by_invalid_id():
    response = client.get_author_by_id(9999)
    assert response.status_code == 404

@allure.feature("Authors API")
@allure.story("Create a new author")
def test_create_author():
    payload = {
        "id": 2001,
        "idBook": 1,
        "firstName": "John",
        "lastName": "Doe"
    }
    response = client.create_author(payload)
    assert response.status_code == 200
    assert response.json()['firstName'] == "John"

@allure.feature("Authors API")
@allure.story("Create author with missing fields")
def test_create_author_missing_fields():
    payload = {"id": 2002}
    response = client.create_author(payload)
    assert response.status_code == 400

@allure.feature("Authors API")
@allure.story("Update existing author")
def test_update_author():
    payload = {
        "id": 1,
        "idBook": 1,
        "firstName": "Updated",
        "lastName": "Author"
    }
    response = client.update_author(1, payload)
    assert response.status_code == 200
    assert response.json()['firstName'] == "Updated"

@allure.feature("Authors API")
@allure.story("Update author with invalid ID")
def test_update_author_invalid_id():
    payload = {
        "id": 9999,
        "idBook": 1,
        "firstName": "Invalid",
        "lastName": "Author"
    }
    response = client.update_author(9999, payload)
    assert response.status_code == 404

@allure.feature("Authors API")
@allure.story("Delete existing author")
def test_delete_author():
    response = client.delete_author(2001)
    assert response.status_code == 200

@allure.feature("Authors API")
@allure.story("Delete author with invalid ID")
def test_delete_author_invalid_id():
    response = client.delete_author(9999)
    assert response.status_code == 404

@allure.feature("Authors API")
@allure.story("Create duplicate author")
def test_create_duplicate_author():
    payload = {
        "id": 1,
        "idBook": 1,
        "firstName": "Duplicate",
        "lastName": "Author"
    }
    response = client.create_author(payload)
    assert response.status_code in [400, 409]