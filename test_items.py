import conftest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from parametrization import Parametrization
import time


def test_set_language_and_chek_button(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(url)
    time.sleep(10)
    button = browser.find_element_by_css_selector("#add_to_basket_form>button")
    print(button.text)
    assert button.is_enabled()
