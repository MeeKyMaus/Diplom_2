import pytest
from helpers.api_requests import create_user, login_user
import random
import string

@pytest.fixture(scope="function")
def user_data():
    email = f"test_{random.randint(1000, 9999)}@example.com"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    name = "TestUser"
    return {"email": email, "password": password, "name": name}

@pytest.fixture(scope="function")
def auth_token(user_data):
    create_response = create_user(user_data["email"], user_data["password"], user_data["name"])
    assert create_response.status_code == 200, f"User creation failed: {create_response.text}"
    login_response = login_user(user_data["email"], user_data["password"])
    assert login_response.status_code == 200, f"Login failed: {login_response.text}"
    return login_response.json().get("accessToken")
