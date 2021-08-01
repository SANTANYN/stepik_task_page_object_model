import pages.main_page
from pages.main_page import MainPage
import conftest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.base_page import BasePage
bugged_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(bugged_link, marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_add_product_to_basket(browser, link):
    browser.implicitly_wait(5)
    product_page_url = link
    product_page = ProductPage(browser, product_page_url)
    product_page.open()
    product_page.check_product_page_url()
    product_page.click_be_button_add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_success_add_to_basket()

