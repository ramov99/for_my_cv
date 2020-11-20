from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_basket_page(browser):
    # Arrange
    main_page = MainPage(browser, MainPage.MAIN_PAGE_LINK)
    main_page.open()

    # Act
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)

    # Assert
    basket_page.verify_basket_page()
    basket_page.user_can_go_back_to_main_page()
    basket_page = MainPage(browser, browser.current_url)
    basket_page.should_be_login_link()


def test_user_can_go_to_basket_page(browser):
    # Arrange
    main_page = MainPage(browser, MainPage.MAIN_PAGE_LINK)
    main_page.open()
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.sign_in_registered_user()
    login_page.should_be_authorized_user()

    # Act
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)

    # Assert
    basket_page.verify_basket_page()
    basket_page.user_can_go_back_to_main_page()
    basket_page = MainPage(browser, browser.current_url)
    basket_page.should_be_login_link()
