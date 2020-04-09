from pages.basket_page import BasketPage
from commons.constants import Url

URL = Url.BASKET_PAGE


def test_basket_is_empty_on_first_opening(browser):
    basket_page = BasketPage(browser, URL)
    basket_page.open()
    basket_page.should_be_empty()
