from playwright.sync_api import Page, expect


def test_homepage_loads(page: Page, website_url: str) -> None:
    page.goto(website_url)

    # Verify URL and page title
    expect(page).to_have_url(website_url)
    expect(page).to_have_title(
        "All products | Books to Scrape - Sandbox"
    )

    # Verify every visible heading has non-empty text
    headings = page.locator("h1, h2, h3, h4, h5, h6")

    for heading in headings.all():
        if heading.is_visible():
            text = heading.inner_text().strip()
            assert text, "A visible heading has empty text"

    # Verify the books section contains at least one book
    books = page.locator("article.product_pod")

    expect(books.first).to_be_visible()
    assert books.count() > 0, "No books found on the homepage"