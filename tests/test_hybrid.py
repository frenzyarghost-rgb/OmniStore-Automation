# tests/test_hybrid.py
import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.api
def test_api_create_and_ui_verify(playwright, search_page):
    # --- PART 1: API SETUP (Fast) ---
    api_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    # We "Create" a post with a unique ID (simulating a product)
    new_post = {
        "title": "OmniStore-Test-Item-99",
        "body": "Hybrid Automation Test",
        "userId": 1
    }
    response = api_context.post("/posts", data=new_post)
    assert response.status == 201

    # Get the title we just created to search for it in the UI
    created_title = response.json()["title"]
    print(f"\n🚀 API Created: {created_title}")

    # --- PART 2: UI VERIFICATION (Accurate) ---
    # Use our existing SearchPage fixture (it already navigated to DuckDuckGo)
    search_page.search_for_term(created_title)

    # Verify the UI reflects what the API did
    # Note: Since JSONPlaceholder is a mock API, it won't actually
    # show up on DuckDuckGo, so we expect a "No results" or the title match.
    expect(search_page.page).to_have_title(f"{created_title} at DuckDuckGo")

    api_context.dispose()