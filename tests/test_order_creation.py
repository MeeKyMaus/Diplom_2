import pytest
from helpers.api_requests import create_order, get_ingredients

class TestOrderCreation:

    def test_create_order_authorized(self, auth_token):
        ingredients_response = get_ingredients()
        ingredient_ids = [ingredient["_id"] for ingredient in ingredients_response.json()["data"]]
        response = create_order(auth_token, ingredient_ids)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json()["success"] is True

    def test_create_order_no_ingredients(self, auth_token):
        response = create_order(auth_token, [])
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
        assert response.json()["message"] == "Ingredient ids must be provided"

    def test_create_order_invalid_ingredient(self, auth_token):
        response = create_order(auth_token, ["invalid_id"])
        assert response.status_code == 500, f"Expected 500, got {response.status_code}"
