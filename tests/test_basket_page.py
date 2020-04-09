from pages.basket_page import BasketPage

URL = "http://selenium1py.pythonanywhere.com/en-gb/basket/"


def test_basket_is_empty_on_first_opening(browser):
    basket_page = BasketPage(browser, URL)
    basket_page.open()
    basket_page.should_be_empty()
