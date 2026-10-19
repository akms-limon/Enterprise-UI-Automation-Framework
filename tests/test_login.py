from playwright.sync_api import Page, expect
from tests.pages.login_page import LoginPage


def test_login_page_navigation(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.open()

    expect(page).to_have_url(LoginPage.URL)
    expect(login_page.login_link).to_be_visible()
    expect(login_page.login_link).to_be_enabled()

    login_page.navigate_to_login()

    expect(page).to_have_url(LoginPage.LOGIN_URL)
    expect(login_page.username).to_be_visible()
    expect(login_page.password).to_be_visible()


def test_login_and_logout_link(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.open()
    login_page.navigate_to_login()

    login_page.login("test_user", "test_password")

    expect(login_page.logout_link).to_be_visible()
    expect(login_page.logout_link).to_be_enabled()
