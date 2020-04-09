import time

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
