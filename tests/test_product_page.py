import time

import pytest

from commons.constants import Url
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

URL = Url.PRODUCT_PAGE


@pytest.mark.guest
class TestGuestOnProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        product_page = ProductPage(browser, URL)
        product_page.open()
        product_page.should_have_login_link()

    def test_guest_can_open_login_page_from_product_page(self, browser):
        product_page = ProductPage(browser, URL)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, URL)
        product_page.open()
        product_name = product_page.get_product_name()
        product_price = product_page.get_product_price()
        product_page.add_product_to_basket()
        product_page.product_success_message_should_have(product_name)
        product_page.basket_total_should_be_equal(product_price)

    def test_guest_does_not_see_success_message_on_page_opening(self, browser):
        product_page = ProductPage(browser, URL)
        product_page.open()
        product_page.should_not_display_success_message()

    def test_guest_can_open_basket_from_product_page(self, browser):
        product_page = ProductPage(browser, URL)
        product_page.open()
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()


@pytest.mark.user
class TestUserProductPage:
    # setup should be replaced with api call
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        time_stamp = str(time.time())
        email = time_stamp + "@fakemail.com"
        password = time_stamp
        login_page = LoginPage(browser, Url.LOGIN_PAGE)
        login_page.open()
        login_page.register_user(email, password)

    def test_user_does_not_see_success_message_on_page_opening(self, browser):
        product_page = ProductPage(browser, URL)
        product_page.open()
        time.sleep(10)
        product_page.should_not_display_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, URL)
        product_page.open()
        product_name = product_page.get_product_name()
        product_price = product_page.get_product_price()
        product_page.add_product_to_basket()
        product_page.product_success_message_should_have(product_name)
        product_page.basket_total_should_be_equal(product_price)
