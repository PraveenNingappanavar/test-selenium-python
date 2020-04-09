from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.find_element(ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def get_product_name(self):
        return self.find_element(ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.find_element(ProductPageLocators.PRODUCT_PRICE).text

    def product_success_message_should_have(self, product_name):
        assert product_name in self.find_element(ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE).text

    def basket_total_should_be_equal(self, product_price):
        assert product_price in self.find_element(ProductPageLocators.BASKET_TOTAL_MESSAGE).text
