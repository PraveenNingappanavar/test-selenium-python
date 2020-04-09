import math

from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # page methods
    def open(self):
        print(f"Opening page with url {self.url}")
        self.browser.get(self.url)

    def go_to_login_page(self):
        self.find_element(BasePageLocators.LOGIN_LINK).click()
        print("Navigating to login page")

    def go_to_basket_page(self):
        self.find_element(BasePageLocators.BASKET_BUTTON).click()
        print("Navigating to basket page")

    def should_have_login_link(self):
        print("Checking if login link is displayed on main page")
        assert self.find_element(BasePageLocators.LOGIN_LINK).is_displayed(), "Login link is not displayed"

    # methods to work with elements
    def find_element(self, locator, time=10):
        print(f"..trying to find element by locator {locator}")
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       f"Can't find element by locator {locator}")

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def element_is_not_present(self, locator, timeout=4):
        try:
            print(f"..checking if {locator} is not present")
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True

        return False

    def element_is_disappeared(self, locator, timeout=4):
        try:
            print(f"..waiting for {locator} is disappeared")
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True
