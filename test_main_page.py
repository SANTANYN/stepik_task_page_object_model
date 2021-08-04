import pytest
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage

"""pytest -v --tb=line --language=en test_login_page.py
"""


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


@pytest.mark.login_guest
class TestLoginFromMainPage:
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()



def test_should_see_auth_page_url(browser):
    login_page_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
    login_page = LoginPage(browser, login_page_url)
    login_page.open()
    login_page.should_be_login_url()


def test_should_see_login_form_in_page(browser):
    login_page_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
    auth_page = LoginPage(browser, login_page_url)
    auth_page.open()
    auth_page.should_be_login_form()
    auth_page.chek_email_in_login_form()
    auth_page.chek_password_in_login_form()


def test_should_see_register_form_in_page(browser):
    browser.implicitly_wait(5)
    login_page_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
    auth_page = LoginPage(browser, login_page_url)
    auth_page.open()
    auth_page.should_be_register_form()
    auth_page.chek_email_field_in_register_form()
    auth_page.chek_password_field_in_register_form()
    auth_page.chek_re_password_field_in_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.should_be_button_to_basket_on_page()
    basket_page.should_be_correct_url_on_basket_page()
    basket_page.check_alert_if_basket_is_empty()
