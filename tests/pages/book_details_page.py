"""Page object for an individual book's details page."""

from playwright.sync_api import Page


class BookDetailsPage:
    """Provide locators and navigation for book details."""

    def __init__(self, page: Page) -> None:
        """Initialize locators for the selected book's information."""
        self.page = page
        self.title = page.locator("div.product_main h1")
        self.price = page.locator("div.product_main .price_color")
        self.book_information = page.locator("div.product_main")

    def go_back(self) -> None:
        """Return to the previous browser history entry."""
        self.page.go_back()
