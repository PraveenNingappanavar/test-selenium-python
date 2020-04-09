import pytest

from pages.basket_page import BasketPage


@pytest.mark.smoke
@pytest.mark.basket_flow
def test_basket_is_empty_on_first_opening(browser):
    basket_page = BasketPage(browser)
    basket_page.open()
    basket_page.should_be_empty()
