# tests/test_hybrid.py
import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.api
# 1. ADD 'page' here so we can navigate
def test_api_create_and_ui_verify(playwright, page, search_page):
    # --- PART 1: API SETUP (Fast) ---
    api_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    new_post = {
        "title": "OmniStore-Test-Item-99",
        "body": "Hybrid Automation Test",
        "userId": 1
    }
    response = api_context.post("/posts", data=new_post)
    assert response.status == 201

    created_title = response.json()["title"]
    print(f"\n🚀 API Created: {created_title}")

    # --- PART 2: UI VERIFICATION (Accurate) ---
    # 2. Tell the browser to go to the site FIRST
    page.goto("https://www.duckduckgo.com")

    # 3. Now search for the term we got from the API
    search_page.search_for_term(created_title)

    # 4. Verify the title matches
    expect(page).to_have_title(f"{created_title} at DuckDuckGo")

    api_context.dispose()