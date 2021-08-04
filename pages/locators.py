from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    SUCCESS_ALERT_AFTER_ADD_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner div.row div.col-sm-6.product_main h1")
    PRODUCT_COASTS = (By.CSS_SELECTOR, "#content_inner  div.col-sm-6.product_main p.price_color")
    PRODUCT_COASTS_IN_ALERT = (By.CSS_SELECTOR,
                               "#messages div.alert.alert-safe.alert-noicon.alert-info.fade.in p:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BUTTON_TO_BASKET = (By.CSS_SELECTOR, "#default div.basket-mini.pull-right.hidden-xs span a")
    CHECK_ALERT_IN_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
