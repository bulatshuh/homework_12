from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def visit_marketplace(self):
        visit_marketplace_button = self.browser.find_element(*MainPageLocators.VISIT_MARKETPLACE_BUTTON)
        visit_marketplace_button.click()
