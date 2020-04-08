from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        return "login" in self.browser.current_url()
