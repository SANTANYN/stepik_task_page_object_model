import conftest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from parametrization import Parametrization
import time
"""pytest -v --tb=line --language=en test_login_page.py
"""


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    time.sleep(30)
    login_link.click()
