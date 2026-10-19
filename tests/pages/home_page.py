"""Page object for the Books to Scrape homepage."""

import random

from playwright.sync_api import Locator, Page


class HomePage:
    """Expose homepage locators and common book-list interactions."""

    URL = "https://books.toscrape.com/index.html"
    TITLE = "All products | Books to Scrape - Sandbox"

    def __init__(self, page: Page) -> None:
        """Initialize homepage locators from a Playwright page."""
        self.page = page
        self.headings = page.locator("h1, h2, h3, h4, h5, h6")
        self.book_cards = page.locator("article.product_pod")
        self.book_title_links = page.locator("article.product_pod h3 a")

    def open(self) -> None:
        """Navigate to the homepage."""
        self.page.goto(self.URL)

    def select_random_books(self, limit: int = 5) -> list[Locator]:
        """Return up to the requested number of random book cards."""
        books = self.book_cards.all()

        assert books, "No books are available on the homepage"

        return random.sample(books, min(limit, len(books)))

    def get_book_title_link(self, book: Locator) -> Locator:
        """Locate the title link inside a book card."""
        return book.locator("h3 a")

    def return_to_homepage(self) -> None:
        """Use browser history to return to the previous page."""
        self.page.go_back()
