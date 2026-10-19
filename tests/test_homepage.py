"""Tests for the Books to Scrape homepage."""

from playwright.sync_api import Page, expect

from tests.pages.home_page import HomePage


def test_homepage_loads(page: Page) -> None:
    """Verify the homepage title, headings, and book listing."""
    home_page = HomePage(page)
    home_page.open()

    expect(page).to_have_url(home_page.URL)
    expect(page).to_have_title(home_page.TITLE)

    for heading in home_page.headings.all():
        if heading.is_visible():
            assert heading.inner_text().strip(), (
                "A visible heading has empty text"
            )

    expect(home_page.book_cards.first).to_be_visible()
    assert home_page.book_cards.count() > 0, "No books found"
