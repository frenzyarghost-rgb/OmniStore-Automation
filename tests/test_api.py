# tests/test_api.py
import pytest


@pytest.mark.api

# --- Your Step 2 Code (GET) ---
def test_get_product_details(playwright):
    api_request_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    response = api_request_context.get("/posts/1")
    assert response.ok
    assert response.json()["id"] == 1
    api_request_context.dispose()

# --- Your Step 3 Code (POST) ---
def test_create_new_order(playwright):
    api_request_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    new_order_data = {
        "title": "Gaming Monitor",
        "body": "4K 144Hz",
        "userId": 1
    }
    response = api_request_context.post("/posts", data=new_order_data)
    assert response.status == 201
    assert response.json()["title"] == "Gaming Monitor"
    api_request_context.dispose()