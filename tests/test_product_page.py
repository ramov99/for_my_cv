import pytest
from pages.product_page import ProductPage
from pages.offer_page import OfferPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from tests.random_credentials import random_string, random_email


class TestGuestAddToBasketFromProductPage:

    @pytest.mark.parametrize('offer_link', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                            "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                            "?promo=offer6", pytest.param("?promo=offer7",
                                                                          marks=pytest.mark.xfail(reason="won't fix")),
                                            "?promo=offer8", "?promo=offer9"])
    def test_guest_can_add_promo_product_to_basket(self, browser, offer_link):
        # Arrange
        offer_page = OfferPage(browser, offer_link)
        offer_page.open()

        # Act
        item_title = offer_page.get_item_title_as_text()
        item_price = offer_page.get_item_price_as_text()
        offer_page.add_to_cart()
        offer_page.solve_quiz_and_get_code()

        # Assert
        offer_page.verify_add_to_basket_notification(item_title, item_price)

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser)
        product_page.open()

        # Act
        product_page.add_to_cart()

        # Assert
        product_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        product_page = ProductPage(browser)

        # Act
        product_page.open()

        # Assert
        product_page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser)
        product_page.open()

        # Act
        product_page.add_to_cart()

        # Assert
        product_page.success_message_should_disappear()


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    page = MainPage(browser, ProductPage.PRODUCT_PAGE_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.register_new_user(random_email(7, 4, 3), random_string(10))
    login_page.should_be_authorized_user()


class TestUserAddToBasketFromProductPage:
    def test_user_cant_see_success_message(self, browser):
        # Arrange
        product_page = ProductPage(browser)

        # Act
        product_page.open()

        # Assert
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser)
        product_page.open()

        # Act
        item_title = product_page.get_item_title_as_text()
        item_price = product_page.get_item_price_as_text()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()

        # Assert
        product_page.verify_add_to_basket_notification(item_title, item_price)
