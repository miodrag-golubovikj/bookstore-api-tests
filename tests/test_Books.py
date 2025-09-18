import pytest
import allure
from src.clients.books_client import BooksClient
from src.utils.debug import log_response, log_request_payload

client = BooksClient()

@allure.feature("Books API")
@allure.story("Retrieve all books")
def test_get_all_books():
    response = client.get_all_books()
    log_response(response, "GET /Books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@allure.feature("Books API")
@allure.story("Retrieve book by valid ID")
def test_get_book_by_valid_id():
    response = client.get_book_by_id(1)
    log_response(response, "GET /Books/1")
    assert response.status_code == 200
    assert response.json()['id'] == 1

@allure.feature("Books API")
@allure.story("Retrieve book by invalid ID")
def test_get_book_by_invalid_id():
    response = client.get_book_by_id(9999)
    log_response(response, "GET /Books/9999")
    assert response.status_code == 404

@allure.feature("Books API")
@allure.story("Create a New Robot Book")
def test_create_book():
    payload = {
        "id": 1001,
        "title": "New Robot Book",
        "description": "Test book",
        "pageCount": 123,
        "excerpt": "Excerpt",
        "publishDate": "2025-09-17T00:00:00Z"
    }
    log_request_payload(payload)
    response = client.create_book(payload)
    log_response(response, "POST /Books")
    assert response.status_code == 200
    assert response.json()['title'] == "New Robot Book"

@allure.feature("Books API")
@allure.story("Create book with missing fields")
def test_create_book_with_missing_fields():
    payload = {"id": 1002}
    log_request_payload(payload)
    response = client.create_book(payload)
    log_response(response, "POST /Books (missing fields)")
    assert response.status_code == 400

@allure.feature("Books API")
@allure.story("Update existing book")
def test_update_book():
    payload = {
        "id": 1,
        "title": "Updated Title",
        "description": "Updated",
        "pageCount": 321,
        "excerpt": "Updated excerpt",
        "publishDate": "2025-09-17T00:00:00Z"
    }
    log_request_payload(payload)
    response = client.update_book(1, payload)
    log_response(response, "PUT /Books/1")
    assert response.status_code == 200
    assert response.json()['title'] == "Updated Title"

@allure.feature("Books API")
@allure.story("Update book with invalid ID")
def test_update_book_invalid_id():
    payload = {
        "id": 9999,
        "title": "Invalid Update",
        "description": "Invalid",
        "pageCount": 0,
        "excerpt": "None",
        "publishDate": "2025-09-17T00:00:00Z"
    }
    log_request_payload(payload)
    response = client.update_book(9999, payload)
    log_response(response, "PUT /Books/9999")
    assert response.status_code == 404

@allure.feature("Books API")
@allure.story("Delete existing book")
def test_delete_book():
    response = client.delete_book(1001)
    log_response(response, "DELETE /Books/1001")
    assert response.status_code == 200

@allure.feature("Books API")
@allure.story("Delete book with invalid ID")
def test_delete_book_invalid_id():
    response = client.delete_book(9999)
    log_response(response, "DELETE /Books/9999")
    assert response.status_code == 404

@allure.feature("Books API")
@allure.story("Create duplicate book")
def test_create_duplicate_book():
    payload = {
        "id": 1,
        "title": "Duplicate",
        "description": "Duplicate",
        "pageCount": 100,
        "excerpt": "Duplicate",
        "publishDate": "2025-09-17T00:00:00Z"
    }
    log_request_payload(payload)
    response = client.create_book(payload)
    log_response(response, "POST /Books (duplicate)")
    assert response.status_code in [400, 409]