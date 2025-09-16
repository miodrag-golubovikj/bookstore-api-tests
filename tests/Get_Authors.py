import pytest
from api.authors import AuthorsAPI
from utils.data_generator import generate_author_payload

@pytest.fixture
def author():
    payload = generate_author_payload()
    response = AuthorsAPI.create(payload)
    assert response.status_code == 200
    yield payload
    AuthorsAPI.delete(payload["id"])

def test_get_all_authors():
    response = AuthorsAPI.get_all()
    assert response.status_code == 200

def test_create_author():
    payload = generate_author_payload()
    response = AuthorsAPI.create(payload)
    assert response.status_code == 200
    AuthorsAPI.delete(payload["id"])