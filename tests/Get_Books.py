import pytest
from api.books import BooksAPI
from utils.data_generator import generate_book_payload

@pytest.fixture
def book():
    payload = generate_book_payload()
    response = BooksAPI.create(payload)
    assert response.status_code == 200
    yield payload
    BooksAPI.delete(payload["id"])

def test_get_all_books():
    response = BooksAPI.get_all()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_book_by_valid_id(book):
    response = BooksAPI.get_by_id(book["id"])
    assert response.status_code == 200
    assert response.json()["title"] == book["title"]

def test_get_book_by_invalid_id():
    response = BooksAPI.get_by_id(-1)
    assert response.status_code == 404

def test_create_book_with_valid_data():
    payload = generate_book_payload()
    response = BooksAPI.create(payload)
    assert response.status_code == 200
    BooksAPI.delete(payload["id"])

def test_update_book(book):
    book["title"] = "Updated Title"
    response = BooksAPI.update(book["id"], book)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"

def test_delete_book():
    payload = generate_book_payload()
    create_resp = BooksAPI.create(payload)
    assert create_resp.status_code == 200
    delete_resp = BooksAPI.delete(payload["id"])
    assert delete_resp.status_code == 200