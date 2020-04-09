from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_have_login_form()
        self.should_have_register_form()

    def should_be_login_url(self):
        print("Checking that url should have 'login'")
        assert "login" in self.browser.current_url

    def should_have_login_form(self):
        print("Checking that login form is displayed")
        assert self.find_element(LoginPageLocators.LOGIN_FORM).is_displayed(), "Login form is not displayed"

    def should_have_register_form(self):
        print("Checking that register form is displayed")
        assert self.find_element(LoginPageLocators.REGISTER_FORM).is_displayed(), "Register form is not displayed"
