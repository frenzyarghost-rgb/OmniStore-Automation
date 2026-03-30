# tests/test_smoke.py
import pytest
from pages.search_page import SearchPage
import os
import json

from playwright.sync_api import expect


#Helper to read JSON
def load_test_data():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "test_data.json")
    with open(file_path) as f:
        data = json.load(f)
        return [item['term'] for item in data]

@pytest.mark.ui
# This decorator tells pytest to run the test 3 times with these inputs
@pytest.mark.parametrize("search_term", load_test_data())
def test_duckduckgo_json_driven(search_page, search_term):
    search_page.search_for_term(search_term)

    # Use 'expect' instead of 'assert'.
    # This will retry for up to 5 seconds if the title isn't right yet!
    expect(search_page.page).to_have_title(f"{search_term} at DuckDuckGo")
    print(f"\n✅ Successfully searched for: {search_term}")