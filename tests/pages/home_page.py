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
        self.product_images = page.locator("article.product_pod img")
        self.next_page_link = page.locator("li.next a")

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

    def get_book_price(self, book: Locator) -> Locator:
        """Locate the displayed price inside a book card."""
        return book.locator(".price_color")

    def has_next_page(self) -> bool:
        """Check whether an enabled next-page link is available."""
        return self.next_page_link.is_visible() and self.next_page_link.is_enabled()

    def go_to_next_page(self) -> None:
        """Navigate to the next page of the book catalog."""
        self.next_page_link.click()
