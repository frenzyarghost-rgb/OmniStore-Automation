import sys
import os
import allure
import pytest
from playwright.sync_api import Page
# Import your Page Object
from pages.search_page import SearchPage

# 1. Keep this for your Path/Imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 2. DELETE the 'def browser' fixture entirely.
# Let Playwright's built-in engine handle it.

# 3. Use the built-in 'page' fixture to set up your SearchPage
@pytest.fixture
def search_page(page):
    search = SearchPage(page)
    # Now we pull the URL from the environment!
    url = os.getenv("BASE_URL")
    search.navigate(url)
    return search

# 4. Keep your screenshot hook (I combined your two duplicate hooks into one)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get('page')
        if page:
            screenshot = page.screenshot(full_page=True)
            allure.attach(screenshot, name="Failure_Screenshot", attachment_type=allure.attachment_type.PNG)