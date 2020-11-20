from pages.base_page import BasePage
from .locators import MainPageLocators, CataloguePageLocators
from selenium.common.exceptions import NoSuchElementException


class CataloguePage(BasePage):
    CATALOGUE_PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/"

    def __init__(self, browser):
        # Set timeout to 0 since unavailable items are searched for on this page
        # and exceptions are thrown 
        BasePage.__init__(self, browser, self.CATALOGUE_PAGE_LINK, 0)

    def go_to_main_page(self):
        self.browser.find_element(*CataloguePageLocators.BACK_TO_MAIN_PAGE_LINK_NAV).click()

    def switch_to_books_category(self):
        self.browser.find_element(*MainPageLocators.CATALOGUE_BOOKS_BUTTON).click()
        assert "books_2" in self.browser.current_url, \
            "Should be books category in browser url"

    def switch_to_clothing_category(self):
        self.browser.find_element(*MainPageLocators.CATALOGUE_CLOTHING_BUTTON).click()
        assert "clothing_1" in self.browser.current_url, \
            "Should be clothing category in browser url"

    def get_items_availability(self):
        all_items_on_page = self.browser.find_elements(*CataloguePageLocators.PRODUCT_POD_ARTICLE)
        available_items, unavailable_items = [], []
        for item in all_items_on_page:
            try:
                self.find_in_element(item, CataloguePageLocators.AVAILABLE_ITEM_TAG)
            except NoSuchElementException:
                unavailable_items.append(item)
            else:
                available_items.append(item)
        return available_items, unavailable_items

    def get_item_title_as_text(self, parent):
        item_title = self.find_in_element(parent, CataloguePageLocators.ITEM_TITLE)
        return item_title.text

    def get_item_price_as_text(self, parent):
        item_price = self.find_in_element(parent, CataloguePageLocators.ITEM_PRICE)
        return item_price.text

    def add_item_to_cart(self, parent):
        self.find_in_element(parent, CataloguePageLocators.ADD_TO_CART_BUTTON).click()

    def verify_item_added_to_cart(self, item_title, item_price):
        item_in_basket_title_notif = self.browser.find_element(*CataloguePageLocators.ADDED_ITEM_TITLE)
        item_in_basket_price_notif = self.browser.find_element(*CataloguePageLocators.ADDED_ITEM_PRICE)
        assert item_title == item_in_basket_title_notif.text, \
            "Item title should be correctly displayed in the basket"
        assert item_price in item_in_basket_price_notif.text, \
            "Item price should be correctly displayed in the basket"

    def go_to_next_page(self, page_number: int):
        for page in range(1, page_number):
            self.browser.find_element(*CataloguePageLocators.NEXT_PAGE_BUTTON).click()
            page += 1
            assert f"page={page}" in self.browser.current_url, \
                "Page number should be correct"

    def go_to_previous_page(self, page_number: int):
        for page in range(page_number, 1, -1):
            self.browser.find_element(*CataloguePageLocators.PREVIOUS_PAGE_BUTTON).click()
            page -= 1
            assert f"page={page}" in self.browser.current_url, \
                "Page number should be correct"
