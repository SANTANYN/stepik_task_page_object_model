from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    login_email = (By.CSS_SELECTOR, "#id_login-u")
    login_password = (By.CSS_SELECTOR, "#id_login-password")
    registration_email = (By.CSS_SELECTOR, "#id_registration-email")
    registration_password = (By.CSS_SELECTOR, "#id_registration-password1")
    registration_password_repeat = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators:
    add_to_basket_button = (By.CSS_SELECTOR, "#add_to_basket_form button")
    success_alert_after_add_product = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    product_name = (By.CSS_SELECTOR, "#content_inner div.row div.col-sm-6.product_main h1")
    product_coasts = (By.CSS_SELECTOR, "#content_inner  div.col-sm-6.product_main p.price_color")
    product_coasts_in_alert = (By.CSS_SELECTOR,
                               "#messages div.alert.alert-safe.alert-noicon.alert-info.fade.in p:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

