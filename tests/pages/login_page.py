from playwright.sync_api import Page, Locator


class LoginPage:
    URL = "https://quotes.toscrape.com/"
    LOGIN_URL = "https://quotes.toscrape.com/login"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_link = page.get_by_role("link", name="Login")
        self.username: Locator = page.locator("input[name='username']")
        self.password: Locator = page.locator("input[name='password']")
        self.submit_button = page.locator("input[type='submit']")
        self.logout_link = page.get_by_role("link", name="Logout")

    def open(self) -> None:
        self.page.goto(self.URL)

    def navigate_to_login(self) -> None:
        self.login_link.click()

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.submit_button.click()