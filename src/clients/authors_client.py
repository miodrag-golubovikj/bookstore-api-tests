import requests
from src.utils.config_loader import load_config

class AuthorsClient:
    def __init__(self):
        self.base_url = load_config()['base_url']
        self.endpoint = f"{self.base_url}/Authors"

    def get_all_authors(self):
        return requests.get(self.endpoint)

    def get_author_by_id(self, author_id):
        return requests.get(f"{self.endpoint}/{author_id}")

    def create_author(self, payload):
        return requests.post(self.endpoint, json=payload)

    def update_author(self, author_id, payload):
        return requests.put(f"{self.endpoint}/{author_id}", json=payload)

    def delete_author(self, author_id):
        return requests.delete(f"{self.endpoint}/{author_id}")