from pages.locators import MarketPlacePageLocators
from pages.market_place_page import MarketplacePage
import pytest


@pytest.fixture(scope='class')
def open_main_page(browser, get_url):
    page = MarketplacePage(browser, get_url)
    page.open()
    page.go_to_full_screen()
    return page


class TestMarketplacePage:
    def test_marketplace_page_main_elements(self, open_main_page):
        page = open_main_page
        page.go_to_markeplace()

        assert page.element_is_presented(*MarketPlacePageLocators.WELCOME_CONTAINER),\
            'Can\'t find welcome container'
        page.welcome_text_presented()

        assert page.element_is_presented(*MarketPlacePageLocators.FILTER_SEARCH_FIELD), \
            'Can\'t find filter search field'
        assert page.element_is_presented(*MarketPlacePageLocators.SORT_BY_DROPDOWN), \
            'Can\'t find sort by drop-list'
        assert page.element_is_presented(*MarketPlacePageLocators.PICTURE_BANNER), \
            'Can\'t find picture banner'
        assert page.element_is_presented(*MarketPlacePageLocators.ITEM_CARD), \
            'Can\'t find item card'
