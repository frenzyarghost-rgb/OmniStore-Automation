# pages/base_page.py
class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    # Make sure THIS method exists:
    def enter_text(self, locator, text):
        self.page.fill(locator, text)

    def click_element(self, locator):
        self.page.click(locator)