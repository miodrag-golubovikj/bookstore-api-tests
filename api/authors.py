import requests
from utils.config import BASE_URL

class AuthorsAPI:
    endpoint = f"{BASE_URL}/Authors"

    @staticmethod
    def get_all():
        return requests.get(AuthorsAPI.endpoint)

    @staticmethod
    def get_by_id(author_id):
        return requests.get(f"{AuthorsAPI.endpoint}/{author_id}")

    @staticmethod
    def create(author_data):
        return requests.post(AuthorsAPI.endpoint, json=author_data)

    @staticmethod
    def update(author_id, author_data):
        return requests.put(f"{AuthorsAPI.endpoint}/{author_id}", json=author_data)

    @staticmethod
    def delete(author_id):
        return requests.delete(f"{AuthorsAPI.endpoint}/{author_id}")