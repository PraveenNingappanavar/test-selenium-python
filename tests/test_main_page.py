import pytest

from commons.constants import Url
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

URL = Url.MAIN_PAGE


@pytest.mark.guest_flow
class TestGuestLoginOnMainPage:
    def test_guest_should_see_login_link_on_main_page(self, browser):
        main_page = MainPage(browser, URL)
        main_page.open()
        main_page.should_have_login_link()

    @pytest.mark.smoke
    def test_guest_can_open_login_page_from_main_page(self, browser):
        main_page = MainPage(browser, URL)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.smoke
@pytest.mark.basket_flow
def test_guest_can_open_basket_from_main_page(browser):
    main_page = MainPage(browser, URL)
    main_page.open()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
