from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Senior QA Tip: Using Role-based locators is more stable than XPath
        self.search_input = page.get_by_role("combobox", name="Search")

    def search_for_term(self, term):
        # 1. Explicitly wait for the element to be ready for interaction
        self.search_input.wait_for(state="visible", timeout=15000)

        # 2. Fill the search term
        self.search_input.fill(term)

        # 3. Press Enter to submit
        self.page.keyboard.press("Enter")

        # 4. Optional: Wait for the network to be idle so the report screenshot looks clean
        self.page.wait_for_load_state("networkidle")