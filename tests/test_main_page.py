from pages.locators import MainPageLocators
from pages.main_page import MainPage
import pytest


@pytest.fixture(scope='class')
def open_main_page(browser, get_url):
    page = MainPage(browser, get_url)
    page.open()
    page.go_to_full_screen()
    return page


class TestMainPage:
    def test_main_page_main_elements(self, open_main_page):
        page = open_main_page

        assert page.element_is_presented(*MainPageLocators.FREE_DOWNLOAD_BUTTON),\
            'Can not find free download button'
        assert page.element_is_presented(*MainPageLocators.VIEW_DEMO_BUTTON),\
            'Can not find view demo button'
        assert page.element_is_presented(*MainPageLocators.VISIT_MARKETPLACE_BUTTON),\
            'Can not find visit marketplace button'
        assert page.element_is_presented(*MainPageLocators.MARKETPLACE_PICTURE),\
            'Can not find picture for marketplace'
        assert page.element_is_presented(*MainPageLocators.VISIT_ALL_PAYMENT_BUTTON),\
            'Can not find visit all button'

        page.visit_marketplace()
        assert page.wait_element_is_presented(*MainPageLocators.MARKETPLACE_PAGE),\
            'Marketplace page is not opened'
