from pages.register_page import RegisterPage
import pytest
from pages.locators import BasePageLocators


@pytest.fixture(scope='class')
def open_register_page(browser, get_url):
    page = RegisterPage(browser, get_url)
    page.open()
    page.go_to_full_screen()
    page.go_to_register()
    return page


class TestMarketplacePage:
    def test_marketplace_page_main_elements(self, open_register_page):
        page = open_register_page

        assert page.element_is_presented(*BasePageLocators.CHECKING_RUNNER), \
            'Register security checking is not opened'
