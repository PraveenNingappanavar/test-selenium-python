import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        print(f"Opening page with url {self.url}")
        self.browser.get(self.url)

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