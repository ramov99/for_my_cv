from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    # Registered users credentials
    test_user = ["wvcudow@jbm.hsz", "ullwngrzv"]

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_PAGE_URL in self.browser.current_url, \
            f"Login page URL should contain {LoginPageLocators.LOGIN_PAGE_URL}!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), \
            "Login email field should be present!"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            "Login password field should be present!"
        assert self.is_element_present(*LoginPageLocators.SIGNUP_SUBMIT_BUTTON), \
            "Signup submit button should be present!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGNUP_EMAIL), \
            "Signup email field should be present!"
        assert self.is_element_present(*LoginPageLocators.SIGNUP_PASSWORD), \
            "Signup password field should be present!"
        assert self.is_element_present(*LoginPageLocators.SIGNUP_REPEAT_PASSWORD), \
            "Signup repeat password field should be present!"
        assert self.is_element_present(*LoginPageLocators.SIGNUP_SUBMIT_BUTTON), \
            "Signup submit button should be present!"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.SIGNUP_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.SIGNUP_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SIGNUP_REPEAT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SIGNUP_SUBMIT_BUTTON).click()

    def sign_in_registered_user(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(self.test_user[0])
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(self.test_user[1])
        self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
