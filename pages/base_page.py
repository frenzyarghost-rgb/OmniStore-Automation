# pages/base_page.py
class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        # 'networkidle' is the secret sauce. It waits until no new
        # network requests are being made for 500ms.
        self.page.goto(url, wait_until="networkidle")

    def get_title(self):
        return self.page.title()

    # Make sure THIS method exists:
    def enter_text(self, locator, text):
        self.page.fill(locator, text)

    def click_element(self, locator):
        self.page.click(locator)