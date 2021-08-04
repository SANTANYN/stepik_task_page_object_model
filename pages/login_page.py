from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Не тот url/wrong url"

    """Смотрим поля логина/ check login_fields"""

    def should_be_login_form(self):
        assert self.browser.find_element(By.CSS_SELECTOR, "#login_form.well"), "Login_form are not found"

    def chek_email_in_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL), "login email field are not found"

    def chek_password_in_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD), "login password field are not found"

    """Смотрим поля логина/ check login_fields"""

    def should_be_register_form(self):
        assert self.browser.find_element(By.CSS_SELECTOR, "#register_form.well"), "Registration form are not found"

    def chek_email_field_in_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL), "email field are not found"

    def chek_password_field_in_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD), "password field are not found"

    def chek_re_password_field_in_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), "re pass field are not found"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email), "email field are not found"
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password), \
        "password field are not found"

        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT).send_keys(password), \
        "re pass field are not found"

        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
        assert self.is_element_present(*BasePageLocators.USER_ICON)
