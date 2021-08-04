from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_button_to_basket_on_page()
        self.should_be_correct_url_on_basket_page()
        self.check_alert_if_basket_is_empty()

    def should_be_button_to_basket_on_page(self):
        self.browser.find_element(*BasketPageLocators.BUTTON_TO_BASKET).click()

    def should_be_correct_url_on_basket_page(self):
        assert "basket" in self.browser.current_url, "Не тот url/wrong url"

    def check_alert_if_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.CHECK_ALERT_IN_EMPTY_BASKET)
