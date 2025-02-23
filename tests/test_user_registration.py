import pytest
from helpers.api_requests import create_user

class TestUserRegistration:

    def test_create_unique_user(self, user_data):
        response = create_user(user_data["email"], user_data["password"], user_data["name"])
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()["success"] is True

    def test_create_existing_user(self, user_data):
        create_user(user_data["email"], user_data["password"], user_data["name"])
        response = create_user(user_data["email"], user_data["password"], user_data["name"])
        assert response.status_code == 403, f"Expected 403, got {response.status_code}"
        assert response.json()["message"] == "User already exists"

    def test_create_user_missing_field(self):
        response = create_user("", "password", "Username")
        assert response.status_code == 403, f"Expected 403, got {response.status_code}"
        assert response.json()["message"] == "Email, password and name are required fields"
