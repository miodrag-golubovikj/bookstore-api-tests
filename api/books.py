import requests
from utils.config import BASE_URL

class BooksAPI:
    endpoint = f"{BASE_URL}/Books"

    @staticmethod
    def get_all():
        return requests.get(BooksAPI.endpoint)

    @staticmethod
    def get_by_id(book_id):
        return requests.get(f"{BooksAPI.endpoint}/{book_id}")

    @staticmethod
    def create(book_data):
        return requests.post(BooksAPI.endpoint, json=book_data)

    @staticmethod
    def update(book_id, book_data):
        return requests.put(f"{BooksAPI.endpoint}/{book_id}", json=book_data)

    @staticmethod
    def delete(book_id):
        return requests.delete(f"{BooksAPI.endpoint}/{book_id}")