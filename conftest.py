import pytest
from playwright.sync_api import Page
from pages.sign_in_page import SignInPage
from pages.account_page import AccountPage
from pages.collections_eco_friendly_page import EcoFriendly
from pages.sale_page import SalePage
from pages.women_sale_page import WomenSale


@pytest.fixture()
def pw_sign_in_page(page: Page):
    return SignInPage(page)


@pytest.fixture()
def pw_account_page(page: Page):
    return AccountPage(page)


@pytest.fixture()
def pw_eco_friendly(page):
    return EcoFriendly(page)


@pytest.fixture()
def pw_sales_page(page):
    return SalePage(page)


@pytest.fixture()
def pw_women_sale_page(page):
    return WomenSale(page)
