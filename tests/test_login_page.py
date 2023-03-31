from pages.login_page import LoginPage
import pytest
from pages.locators import BasePageLocators


@pytest.fixture(scope='class')
def open_login_page(browser, get_url):
    page = LoginPage(browser, get_url)
    page.open()
    page.go_to_full_screen()
    page.go_to_login()
    return page


class TestMarketplacePage:
    def test_marketplace_page_main_elements(self, open_login_page):
        page = open_login_page

        assert page.element_is_presented(*BasePageLocators.CHECKING_RUNNER), \
            'Register security checking is not opened'
