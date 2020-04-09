from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        print("Adding product to cart")
        self.find_element(ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def get_product_name(self):
        print("Getting product name")
        product_name = self.find_element(ProductPageLocators.PRODUCT_NAME).text
        print(f"Product name is {product_name}")
        return product_name

    def get_product_price(self):
        print("Getting product price")
        product_price = self.find_element(ProductPageLocators.PRODUCT_PRICE).text
        print(f"Product price is {product_price}")
        return product_price

    def product_success_message_should_have(self, product_name):
        print(f"Checking that {product_name} is displayed in success message")
        assert product_name in self.find_element(ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE).text

    def basket_total_should_be_equal(self, product_price):
        print(f"Checking that basket total equals {product_price}")
        assert product_price in self.find_element(ProductPageLocators.BASKET_TOTAL_MESSAGE).text
