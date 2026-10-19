from playwright.sync_api import Page, expect


def test_homepage_loads(page: Page, website_url: str) -> None:
    page.goto(website_url)

    expect(page).to_have_url(website_url)
    expect(page).to_have_title(
        "All products | Books to Scrape - Sandbox"
    )