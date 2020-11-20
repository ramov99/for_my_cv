from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    BASKET_PAGE_LINK = "http://selenium1py.pythonanywhere.com/basket/"

    def verify_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER)
        assert "basket" in self.browser.current_url, \
            "The page url should contain 'basket', but it doesn't"

    def user_can_go_back_to_main_page(self):
        assert self.is_element_present(*BasketPageLocators.BACK_TO_MAIN_PAGE_LINK_NAV), \
            "Back to main page button should be present in the navbar"
        assert self.is_element_present(*BasketPageLocators.BACK_TO_MAIN_PAGE_LINK_CONTENT), \
            "Back to main page button should be present in the page content"
