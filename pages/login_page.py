from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Не тот url/wrong url"

    """Смотрим поля логина/ check login_fields"""
    def should_be_login_form(self):
        assert self.browser.find_element(By.CSS_SELECTOR, "#login_form.well"), "Login_form are not found"

    def chek_email_in_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.login_email), "login email field are not found"

    def chek_password_in_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.login_password), "login password field are not found"

    """Смотрим поля логина/ check login_fields"""
    def should_be_register_form(self):
        assert self.browser.find_element(By.CSS_SELECTOR, "#register_form.well"), "Registration form are not found"

    def chek_email_field_in_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.registration_email), "email field are not found"

    def chek_password_field_in_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.registration_password), "password field are not found"

    def chek_re_password_field_in_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.registration_password_repeat), "re pass field are not found"
