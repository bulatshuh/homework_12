from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):
    def check_text_of_register_welcome(self):
        login_text = self.browser.find_element(*RegisterPageLocators.REGISTER_ACCOUNT_TEXT).text
        assert login_text == 'Register Account', \
            'Wrong register welcome text'
