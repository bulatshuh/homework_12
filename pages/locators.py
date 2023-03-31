from selenium.webdriver.common.by import By


class BasePageLocators:
    REGISTER_BUTTON = (By.CSS_SELECTOR, '.btn.btn-black.navbar-btn')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn.btn-link.navbar-btn')
    MARKETPLACE_BUTTON = (By.CSS_SELECTOR,
                          '.nav.navbar-nav [href="https://www.opencart.com/index.php?route=marketplace/extension"]')
    CHECKING_RUNNER = (By.CSS_SELECTOR, '#challenge-running')


class MainPageLocators:
    FREE_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, '.btn.btn-success.btn-xl')
    VIEW_DEMO_BUTTON = (By.CSS_SELECTOR, '.btn.btn-white.btn-xl')
    VISIT_MARKETPLACE_BUTTON = (By.CSS_SELECTOR, '.btn.btn-primary.btn-xl')
    MARKETPLACE_PICTURE = (By.CSS_SELECTOR, '.col-md-6 .img-responsive')
    VISIT_ALL_PAYMENT_BUTTON = (By.CSS_SELECTOR, '.btn.btn-ghost-dark.btn-lg.hidden-xs')
    MARKETPLACE_PAGE = (By.CSS_SELECTOR, '#fb-root.fb_reset')


class MarketPlacePageLocators:
    WELCOME_CONTAINER = (By.CSS_SELECTOR, '.page-header .container :nth-child(1)')
    FILTER_SEARCH_FIELD = (By.CSS_SELECTOR, '.input-group [name="filter_search"]')
    SORT_BY_DROPDOWN = (By.CSS_SELECTOR, '#input-sort')
    PICTURE_BANNER = (By.CSS_SELECTOR, '.img-responsive[alt="Afterpay"]')
    ITEM_CARD = (By.CSS_SELECTOR, '.row .col-md-4')


class ItemCardPageLocators:
    EXTENSION_SEARCH_FIELD = (By.CSS_SELECTOR, '#extension-search [name="filter_search"]')
    ITEM_PICTURE = (By.CSS_SELECTOR, '.well .img-responsive')
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, '.btn.btn-success.btn-lg.btn-block')
    NUMBER_OF_DOWNLOADS_FIELD = (By.CSS_SELECTOR, '#sales')
    NUMBER_OF_COMMENTS_FIELD = (By.CSS_SELECTOR, '.col-md-4 :nth-child(3)#comment')


class RegisterPageLocators:
    REGISTER_ACCOUNT_TEXT = (By.CSS_SELECTOR, '#content h1')
    FIRSTNAME_FIELD = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    SUBSCRIBE_YES_CHECKBOX = (By.CSS_SELECTOR, '.col-sm-10 .form-check.form-check-inline:nth-child(1)')
    SUBSCRIBE_NO_CHECKBOX = (By.CSS_SELECTOR, '.col-sm-10 .form-check.form-check-inline:nth-child(2)')
    READ_POLICY_CHECKBOX = (By.CSS_SELECTOR, '.float-end.text-right .form-check.form-check-inline')


class LoginPageLocators:
    LOGIN_TEXT = (By.CSS_SELECTOR, '.container h1')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn.btn-primary.btn-lg.hidden-xs')
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.col-sm-6.text-right .btn-link')
