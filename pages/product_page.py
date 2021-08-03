from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.check_product_page_url()
        self.click_be_button_add_to_basket()
        self.should_not_be_success_message()
        self.check_success_add_to_basket()
        self.should_not_be_success_message()
        self.should_disappeared()

    def check_product_page_url(self):
        assert "catalogue" in self.browser.current_url, "wrong url, page not found"

    def click_be_button_add_to_basket(self,):
        add_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        add_button.click()

    def check_success_add_to_basket(self):
        chek_alert = self.browser.find_element(*ProductPageLocators.success_alert_after_add_product).text
        check_name = self.browser.find_element(*ProductPageLocators.product_name).text
        product_coast = self.browser.find_element(*ProductPageLocators.product_coasts).text
        check_product_coasts_in_alert = self.browser.find_element(*ProductPageLocators.product_coasts_in_alert).text
        print(chek_alert)
        print(check_name)
        print(product_coast)
        print(check_product_coasts_in_alert)
        assert chek_alert == check_name
        assert product_coast == check_product_coasts_in_alert

    def should_not_be_success_message(self, timeout=4):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, timeout),\
            "Success message is presented"

    def should_disappeared(self, timeout=4):
        assert self.browser.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, timeout),\
            "Success message is presented"




