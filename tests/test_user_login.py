import pytest
from helpers.api_requests import login_user, create_user

def test_login_valid_user(user_data):
    create_user(user_data["email"], user_data["password"], user_data["name"])
    response = login_user(user_data["email"], user_data["password"])
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["success"] is True

def test_login_invalid_user():
    response = login_user("nonexistent@example.com", "wrongpassword")
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    assert response.json()["message"] == "email or password are incorrect"
