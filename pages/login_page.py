from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def check_text_of_login_welcome(self):
        login_text = self.browser.find_element(*LoginPageLocators.LOGIN_TEXT).text
        assert login_text == 'Log in to your OpenCart account',\
            'Wrong login welcome text'
