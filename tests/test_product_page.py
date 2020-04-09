import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, URL)
    product_page.open()
    product_page.should_have_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, URL)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, URL)
    product_page.open()
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    product_page.add_product_to_basket()
    product_page.product_success_message_should_have(product_name)
    product_page.basket_total_should_be_equal(product_price)


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, URL)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_display_success_message()


def test_success_message_is_not_displayed_on_page_opening(browser):
    product_page = ProductPage(browser, URL)
    product_page.open()
    product_page.should_not_display_success_message()


@pytest.mark.xfail(reason="is being fixed")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, URL)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.success_message_should_disappear()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, URL)
    product_page.open()
    product_page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_empty()
