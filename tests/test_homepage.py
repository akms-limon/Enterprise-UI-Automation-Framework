
from playwright.sync_api import Page, expect


def test_homepage_loads(page: Page) -> None:
    page.goto("https://books.toscrape.com/index.html")

    expect(page).to_have_url(
        "https://books.toscrape.com/index.html"
    )
    expect(page).to_have_title("All products | Books to Scrape - Sandbox")
