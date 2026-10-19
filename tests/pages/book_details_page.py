from playwright.sync_api import Page


class BookDetailsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.locator("div.product_main h1")
        self.book_information = page.locator("div.product_main")
