import pytest

def test_save_storage_state(page):
    # 1. Navigate to login
    page.goto("https://your-omnistore-url.com/login")

    # 2. Perform Login
    page.fill("#username", "your_test_user")
    page.fill("#password", "your_password")
    page.click("#login-button")

    # 3. Wait for the dashboard to confirm login worked
    page.wait_for_selector(".user-profile")

    # 4. Save the "Session" to a JSON file
    page.context.storage_state(path="auth/state.json")