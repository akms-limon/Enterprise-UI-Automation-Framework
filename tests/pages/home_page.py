import random
from playwright.sync_api import Locator, Page


class HomePage:
    URL = "https://books.toscrape.com/index.html"
    TITLE = "All products | Books to Scrape - Sandbox"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.headings = page.locator("h1, h2, h3, h4, h5, h6")
        self.book_cards = page.locator("article.product_pod")
        self.book_title_links = page.locator("article.product_pod h3 a")

    def open(self) -> None:
        self.page.goto(self.URL)

    def select_random_books(self, limit: int = 5) -> list[Locator]:
        books = self.book_cards.all()

        assert books, "No books are available on the homepage"

        return random.sample(books, min(limit, len(books)))

    def get_book_title_link(self, book: Locator) -> Locator:
        return book.locator("h3 a")

    def return_to_homepage(self) -> None:
        self.page.go_back()