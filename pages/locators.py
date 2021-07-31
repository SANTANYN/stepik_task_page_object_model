from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    login_email = (By.CSS_SELECTOR, "#id_login-u")
    login_password = (By.CSS_SELECTOR, "#id_login-password")
    registration_email = (By.CSS_SELECTOR, "#id_registration-email")
    registration_password = (By.CSS_SELECTOR, "#id_registration-password1")
    registration_password_repeat = (By.CSS_SELECTOR, "#id_registration-password2")
