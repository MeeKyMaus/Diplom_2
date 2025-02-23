import pytest
from helpers.api_requests import update_user

class TestUserUpdate:

    def test_update_user_authorized(self, auth_token):
        new_name = "UpdatedName"
        response = update_user(auth_token, {"name": new_name})
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()["user"]["name"] == new_name

    def test_update_user_unauthorized(self):
        response = update_user("", {"name": "Hacker"})
        assert response.status_code == 401, f"Expected 401, got {response.status_code}"
        assert response.json()["message"] == "You should be authorised"
