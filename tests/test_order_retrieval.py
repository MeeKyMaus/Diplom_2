import pytest
from helpers.api_requests import get_user_orders

def test_get_orders_authorized(auth_token):
    response = get_user_orders(auth_token)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "orders" in response.json(), "Response JSON should contain 'orders'"




