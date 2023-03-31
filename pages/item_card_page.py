from .base_page import BasePage
from .locators import ItemCardPageLocators


class ItemCardPage(BasePage):
    def download_item(self):
        download_button = self.browser.find_element(*ItemCardPageLocators.DOWNLOAD_BUTTON)
        download_button.click()
