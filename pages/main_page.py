from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        self.find_element(MainPageLocators.LOGIN_LINK).click()
        return LoginPage(self.browser, self.browser.current_url)

    def should_have_login_link(self):
        assert self.find_element(MainPageLocators.LOGIN_LINK).is_displayed(), "Login link is not displayed"
