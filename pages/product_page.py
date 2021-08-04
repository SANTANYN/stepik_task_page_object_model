from .base_page import BasePage
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
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def check_success_add_to_basket(self):
        chek_alert = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT_AFTER_ADD_PRODUCT).text
        check_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_coast = self.browser.find_element(*ProductPageLocators.PRODUCT_COASTS).text
        check_product_coasts_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_COASTS_IN_ALERT).text
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
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, timeout), \
            "Success message is presented, but should not be"




