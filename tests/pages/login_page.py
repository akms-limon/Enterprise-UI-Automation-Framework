"""Page object for login-related interactions on Quotes to Scrape."""

from playwright.sync_api import Locator, Page


class LoginPage:
    """Expose login form locators and actions."""

    URL = "https://quotes.toscrape.com/"
    LOGIN_URL = "https://quotes.toscrape.com/login"

    def __init__(self, page: Page) -> None:
        """Initialize locators for login, credentials, and logout."""
        self.page = page
        self.login_link = page.get_by_role("link", name="Login")
        self.username: Locator = page.locator("input[name='username']")
        self.password: Locator = page.locator("input[name='password']")
        self.submit_button = page.locator("input[type='submit']")
        self.logout_link = page.get_by_role("link", name="Logout")

    def open(self) -> None:
        """Open the Quotes to Scrape homepage."""
        self.page.goto(self.URL)

    def navigate_to_login(self) -> None:
        """Open the login form from the homepage."""
        self.login_link.click()

    def login(self, username: str, password: str) -> None:
        """Submit the login form with the supplied credentials."""
        self.username.fill(username)
        self.password.fill(password)
        self.submit_button.click()
