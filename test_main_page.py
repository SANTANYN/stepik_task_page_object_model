import pages.main_page
from pages.main_page import MainPage
import conftest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators


"""pytest -v --tb=line --language=en test_login_page.py
"""


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     browser.get(link)
#     login_link = browser.find_element_by_css_selector("#login_link")
#     time.sleep(30)
#     login_link.click()

def test_should_be_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_should_be_see_auth_page_url(browser):
    login_page_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
    login_page = LoginPage(browser, login_page_url)
    login_page.open()
    login_page.should_be_login_url()


def test_should_be_see_login_form_in_page(browser):
    login_page_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
    auth_page = LoginPage(browser, login_page_url)
    auth_page.open()
    auth_page.should_be_login_form()
    auth_page.chek_email_in_login_form()
    auth_page.chek_password_in_login_form()


def test_should_be_see_register_form_in_page(browser):
    login_page_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
    auth_page = LoginPage(browser, login_page_url)
    auth_page.open()
    auth_page.should_be_register_form()
    auth_page.chek_email_field_in_register_form()
    auth_page.chek_password_field_in_register_form()
    auth_page.chek_re_password_field_in_register_form()




