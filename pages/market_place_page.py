from .base_page import BasePage
from .locators import MarketPlacePageLocators


class MarketplacePage(BasePage):
    def welcome_text_presented(self):
        welcome_field_text = self.browser.find_element(*MarketPlacePageLocators.WELCOME_CONTAINER).text
        assert welcome_field_text == 'Welcome to OpenCart Extension Store',\
            'Wrong welcome text'
