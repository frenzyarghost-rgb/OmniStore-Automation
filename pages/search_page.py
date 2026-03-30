# pages/search_page.py
from pages.base_page import BasePage

class SearchPage(BasePage):
    # This XPath covers both the old 'input' and the new 'textarea' Google uses
    SEARCH_INPUT = "//textarea[@name='q'] | //input[@name='q']"

    def search_for_term(self, term):
        # We wait for the element to be visible first - good Senior QA practice!
        self.page.wait_for_selector(self.SEARCH_INPUT)
        self.enter_text(self.SEARCH_INPUT, term)
        self.page.keyboard.press("Enter")