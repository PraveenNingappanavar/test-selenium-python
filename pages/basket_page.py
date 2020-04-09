from commons.constants import Url
from pages.base_page import BasePage
from pages.locators import BasketPageLocators

empty_message_text = "Your basket is empty"
basket_title_text = "Basket"


class BasketPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = Url.BASKET_PAGE

    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_have_basket_title()

    def should_be_empty(self):
        self.should_not_have_items()
        self.should_have_empty_message()

    def should_be_basket_url(self):
        print("Checking that it is basket page url")
        assert "basket" in self.browser.current_url, "Incorrect url for basket page"

    def should_have_basket_title(self):
        print("Checking that basket has title")
        assert basket_title_text in self.find_element(BasketPageLocators.BASKET_TITLE).text,\
            "Basket page has incorrect title"

    def should_not_have_items(self):
        print("Checking that basket doesn't have items")
        assert self.element_is_not_present(BasketPageLocators.BASKET_ITEMS),\
            "Basket has items, but should not"

    def should_have_empty_message(self):
        print("Checking that basket has empty message")
        assert empty_message_text in self.find_element(BasketPageLocators.BASKET_MESSAGE).text,\
            "Empty message is not displayed, but should be"
