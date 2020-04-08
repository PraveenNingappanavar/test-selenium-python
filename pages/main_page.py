from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link").click()