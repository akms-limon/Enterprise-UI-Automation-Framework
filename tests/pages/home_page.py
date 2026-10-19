from playwright.sync_api import Locator, Page


class HomePage:
    URL = "https://books.toscrape.com/index.html"
    TITLE = "All products | Books to Scrape - Sandbox"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.headings = page.locator("h1, h2, h3, h4, h5, h6")
        self.book_cards = page.locator("article.product_pod")

    def open(self) -> None:
        self.page.goto(self.URL)
