import requests

BASE_URL = "https://stellarburgers.nomoreparties.site/api"
AUTH_URL = f"{BASE_URL}/auth"
ORDERS_URL = f"{BASE_URL}/orders"
INGREDIENTS_URL = f"{BASE_URL}/ingredients"

def create_user(email, password, name):
    url = f"{AUTH_URL}/register"
    payload = {"email": email, "password": password, "name": name}
    return requests.post(url, json=payload)

def login_user(email, password):
    url = f"{AUTH_URL}/login"
    payload = {"email": email, "password": password}
    return requests.post(url, json=payload)

def get_user(token):
    url = f"{AUTH_URL}/user"
    headers = {"Authorization": token}
    return requests.get(url, headers=headers)

def update_user(token, data):
    url = f"{AUTH_URL}/user"
    headers = {"Authorization": token}
    return requests.patch(url, json=data, headers=headers)

def create_order(token, ingredients):
    headers = {"Authorization": token} if token else {}
    payload = {"ingredients": ingredients}
    return requests.post(ORDERS_URL, json=payload, headers=headers)

def get_user_orders(token):
    headers = {"Authorization": token}
    return requests.get(ORDERS_URL, headers=headers)

def get_ingredients():
    return requests.get(INGREDIENTS_URL)
