import requests
from src.utils.config_loader import load_config

class BooksClient:
    def __init__(self):
        self.base_url = load_config()['base_url']
        self.endpoint = f"{self.base_url}/Books"

    def get_all_books(self):
        return requests.get(self.endpoint)

    def get_book_by_id(self, book_id):
        return requests.get(f"{self.endpoint}/{book_id}")

    def create_book(self, payload):
        return requests.post(self.endpoint, json=payload)

    def update_book(self, book_id, payload):
        return requests.put(f"{self.endpoint}/{book_id}", json=payload)

    def delete_book(self, book_id):
        return requests.delete(f"{self.endpoint}/{book_id}")