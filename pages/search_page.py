from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Standard DuckDuckGo/Google search input selector
        self.search_input = page.locator('input[name="q"]')

    def search_for_term(self, term):
        # 1. Wait for the element to be ATTACHED to the DOM first
        self.search_input.wait_for(state="attached", timeout=20000)
        # 2. Then ensure it is visible
        self.search_input.wait_for(state="visible", timeout=20000)

        self.search_input.fill(term)
        self.page.keyboard.press("Enter")
        self.page.wait_for_load_state("networkidle")