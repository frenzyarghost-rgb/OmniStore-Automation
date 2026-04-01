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
    return SearchPage(page)

# 4. Keep your screenshot hook (I combined your two duplicate hooks into one)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 1. Try to get the standard 'page' fixture
        page = item.funcargs.get('page')

        # 2. If 'page' is None, try to get it from your 'search_page' fixture
        if not page and 'search_page' in item.funcargs:
            page = item.funcargs.get('search_page').page

        # 3. If we found a page, take the screenshot
        if page:
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name=f"Failed_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )

        # 4. ... inside your if report.failed block ...
        if page:
            # Add a tiny 'Breath' so the browser can render pixels
            page.wait_for_timeout(500)
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name=f"Failed_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )