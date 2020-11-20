from .main_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, ProductPage.PRODUCT_PAGE_LINK)

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.PROMO_ITEM_ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_item_price_as_text(self):
        item_price = self.browser.find_element(*ProductPageLocators.PROMO_ITEM_PRICE)
        return item_price.text

    def get_item_title_as_text(self):
        item_title = self.browser.find_element(*ProductPageLocators.PROMO_ITEM_TITLE)
        return item_title.text

    def verify_add_to_basket_notification(self, item_title, item_price):
        item_in_basket_title_notif = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE)
        item_in_basket_price_notif = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_NOTIFICATION)
        assert item_title == item_in_basket_title_notif.text, \
            "Item title should be correctly displayed in the basket"
        assert item_price in item_in_basket_price_notif.text, \
            "Item price should be correctly displayed in the basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), \
            "Success message is presented"

    def success_message_should_disappear(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), \
            "Success message should disappear" \
