from pages.locators import ItemCardPageLocators
from pages.locators import BasePageLocators
from pages.item_card_page import ItemCardPage
import pytest


@pytest.fixture(scope='class')
def open_item_page(browser, get_url):
    page = ItemCardPage(browser, get_url)
    page.open()
    page.go_to_full_screen()
    page.go_to_markeplace()
    page.open_item_card()
    return page


class TestMarketplacePage:
    def test_marketplace_page_main_elements(self, open_item_page):
        page = open_item_page

        assert page.element_is_presented(*ItemCardPageLocators.DOWNLOAD_BUTTON),\
            'Can\'t find download button'
        assert page.element_is_presented(*ItemCardPageLocators.EXTENSION_SEARCH_FIELD), \
            'Can\'t find extension search field'
        assert page.element_is_presented(*ItemCardPageLocators.ITEM_PICTURE), \
            'Can\'t find items picture'
        assert page.element_is_presented(*ItemCardPageLocators.NUMBER_OF_DOWNLOADS_FIELD), \
            'Can\'t find number of downloads field'
        assert page.element_is_presented(*ItemCardPageLocators.NUMBER_OF_COMMENTS_FIELD), \
            'Can\'t find number of comments'

        page.download_item()
        assert page.wait_element_is_presented(*BasePageLocators.CHECKING_RUNNER),\
            'Register security checking is not opened'
