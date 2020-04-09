import time

import pytest

from commons.constants import Url
from pages.login_page import LoginPage

URL = Url.LOGIN_PAGE


def test_guest_can_register(browser):
    time_stamp = str(time.time())
    email = time_stamp + "@fakemail.com"
    password = time_stamp

    login_page = LoginPage(browser, URL)
    login_page.open()
    login_page.register_user(email, password)
    login_page.user_should_be_authorized()


@pytest.mark.user
class TestRegisteredUser:
    # setup should be replaced with api call
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        time_stamp = str(time.time())
        self.email = time_stamp + "@fakemail.com"
        self.password = time_stamp
        login_page = LoginPage(browser, URL)
        login_page.open()
        login_page.register_user(self.email, self.password)
        login_page.logout_user()

    def test_registered_user_can_login(self, browser):
        login_page = LoginPage(browser, URL)
        login_page.open()
        login_page.login_user(self.email, self.password)
        login_page.user_should_be_authorized()
