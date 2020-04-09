from pages.product_page import ProductPage

URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, URL)
    product_page.open()
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    product_page.add_product_to_cart()

    product_page.product_success_message_should_have(product_name)
    product_page.basket_total_should_be_equal(product_price)
