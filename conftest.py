from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://www.opencart.com',
                     help="Enter base url where you want to send request")

    parser.addoption('--browser', action='store', default='opera',
                     help="Enter browser you want to use")


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption('browser')
    if browser_name == 'chrome':
        print('\nOpening Chrome...')
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('\nOpening Firefox...')
        browser = webdriver.Firefox()
    elif browser_name == 'opera':
        print('\nOpening Opera...')
        # you need to paster your path to opera driver
        browser = webdriver.Chrome('')
    else:
        raise pytest.UsageError('--browser should be chrome, firefox, opera')
    yield browser
    print('\nClosing browser...')
    browser.quit()


@pytest.fixture(scope='session')
def get_url(request):
    user_url = request.config.getoption('url')
    yield user_url
