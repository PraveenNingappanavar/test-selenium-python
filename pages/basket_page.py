from pages.base_page import BasePage
from pages.locators import BasketPageLocators

empty_message_text = "Your basket is empty"


class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_not_have_items()
        self.should_have_empty_message()

    def should_not_have_items(self):
        print("Checking that basket doesn't have items")
        assert self.element_is_not_present(BasketPageLocators.BASKET_ITEMS),\
            "Basket has items, but should not"

    def should_have_empty_message(self):
        print("Checking that basket has empty message")
        assert empty_message_text in self.find_element(BasketPageLocators.BASKET_MESSAGE).text,\
            "Empty message is not displayed, but should be"
