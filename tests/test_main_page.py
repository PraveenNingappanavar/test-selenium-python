from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

URL = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_on_main_page(browser):
    main_page = MainPage(browser, URL)
    main_page.open()
    main_page.should_have_login_link()


def test_guest_can_open_login_page_from_main_page(browser):
    main_page = MainPage(browser, URL)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, URL)
    main_page.open()
    main_page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_empty()
