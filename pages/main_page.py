from .base_page import BasePage
from .locators import MainPageLocators, BasketPageLocators


class MainPage(BasePage):
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"

    def go_to_login_page(self):
        login_page_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_page_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def go_to_basket_page(self):
        basket_page_button = self.browser.find_element(*BasketPageLocators.BASKET_PAGE_LINK)
        basket_page_button.click()

    def go_to_catalogue_page(self):
        catalogue_button = self.browser.find_element(*MainPageLocators.CATALOGUE_BUTTON)
        catalogue_button.click()
