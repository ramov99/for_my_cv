from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = By.CSS_SELECTOR, ".icon-user"


class MainPageLocators:
    LOGIN_LINK = By.CSS_SELECTOR, "#login_link"
    CATALOGUE_BUTTON = By.CSS_SELECTOR, "#browse [href$='catalogue/']"
    CATALOGUE_CLOTHING_BUTTON = By.CSS_SELECTOR, "#browse [href$='clothing_1/']"
    CATALOGUE_BOOKS_BUTTON = By.CSS_SELECTOR, "#browse [href$='books_2/']"
    CATALOGUE_OFFER_BUTTON = By.CSS_SELECTOR, "#browse [href$='offers/']"


class LoginPageLocators:
    LOGIN_PAGE_URL = "accounts/login/"
    SIGNUP_EMAIL = By.CSS_SELECTOR, "#id_registration-email"
    SIGNUP_PASSWORD = By.CSS_SELECTOR, "#id_registration-password1"
    SIGNUP_REPEAT_PASSWORD = By.CSS_SELECTOR, "#id_registration-password2"
    SIGNUP_SUBMIT_BUTTON = By.CSS_SELECTOR, "button[name='registration_submit']"
    LOGIN_EMAIL = By.CSS_SELECTOR, "#id_login-username"
    LOGIN_PASSWORD = By.CSS_SELECTOR, "#id_login-password"
    LOGIN_SUBMIT_BUTTON = By.CSS_SELECTOR, "button[name='login_submit']"
    WELCOME_TEXT = By.CSS_SELECTOR, "div[class='alertinner wicon']"
    LOGOUT_BUTTON = By.CSS_SELECTOR, "#logout_link"


class ProductPageLocators:
    PROMO_ITEM_ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "#add_to_basket_form button"
    PROMO_ITEM_TITLE = By.CSS_SELECTOR, ".product_main > h1"
    PROMO_ITEM_PRICE = By.CSS_SELECTOR, ".product_main > .price_color"
    ITEM_ADDED_MESSAGE = By.CSS_SELECTOR, "#messages > div:nth-child(1) strong"
    BASKET_PRICE_NOTIFICATION = By.CSS_SELECTOR, "#messages > div:last-child .alertinner strong"


class BasketPageLocators:
    BASKET_PAGE_LINK = By.CSS_SELECTOR, ".basket-mini .btn.btn-default[href]"
    BASKET_HEADER = By.CSS_SELECTOR, ".page-header > h1"
    BACK_TO_MAIN_PAGE_LINK_NAV = By.CSS_SELECTOR, ".breadcrumb a[href]"
    BACK_TO_MAIN_PAGE_LINK_CONTENT = By.CSS_SELECTOR, "#content_inner a[href]"


class CataloguePageLocators:
    BACK_TO_MAIN_PAGE_LINK_NAV = By.CSS_SELECTOR, ".breadcrumb a[href]"
    PRODUCT_POD_ARTICLE = By.CSS_SELECTOR, ".product_pod"
    ITEM_TITLE = By.CSS_SELECTOR, "h3 a[title]"
    ITEM_PRICE = By.CSS_SELECTOR, ".product_price p"
    AVAILABLE_ITEM_TAG = By.CSS_SELECTOR, ".icon-ok"
    UNAVAILABLE_ITEM_TAG = By.CSS_SELECTOR, ".outofstock.availability .icon-remove"
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "button[type='submit']"
    NEXT_PAGE_BUTTON = By.CSS_SELECTOR, ".next a[href]"
    PREVIOUS_PAGE_BUTTON = By.CSS_SELECTOR, ".previous a[href]"
    ADDED_ITEM_TITLE = By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong"
    ADDED_ITEM_PRICE = By.CSS_SELECTOR, ".alert:nth-child(3) .alertinner strong"
