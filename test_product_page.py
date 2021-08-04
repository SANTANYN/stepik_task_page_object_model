import pytest
import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
bugged_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"




@pytest.mark.xfail
def test_is_not_element_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page_url = link
    product_page = ProductPage(browser, product_page_url)
    product_page.open()
    product_page.check_product_page_url()
    product_page.click_be_button_add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_success_add_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_is_disappeared(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page_url = link
    product_page = ProductPage(browser, product_page_url)
    product_page.open()
    product_page.check_product_page_url()
    product_page.click_be_button_add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_success_add_to_basket()
    product_page.should_disappeared()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.should_be_button_to_basket_on_page()
    basket_page.should_be_correct_url_on_basket_page()
    basket_page.check_alert_if_basket_is_empty()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    product_page_url = link
    product_page = ProductPage(browser, product_page_url)
    product_page.open()
    product_page.check_product_page_url()
    product_page.click_be_button_add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_success_add_to_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = f'{time.time()}@mail.ru'
        password = f'{time.time()}+12345678999'
        link_reg = "http://selenium1py.pythonanywhere.com/accounts/login"
        log_page = LoginPage(browser, link_reg)
        log_page.open()
        log_page.register_new_user(email, password)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        product_page_url = link
        product_page = ProductPage(browser, product_page_url)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(bugged_link, marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer10"])
    @pytest.mark.need_review
    def test_user_add_product_to_basket(self, browser, link):
        product_page_url = link
        product_page = ProductPage(browser, product_page_url)
        product_page.open()
        product_page.check_product_page_url()
        product_page.click_be_button_add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.check_success_add_to_basket()
