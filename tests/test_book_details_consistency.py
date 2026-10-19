"""Tests for consistency of homepage and book-details information."""

from playwright.sync_api import Page, expect

from tests.pages.book_details_page import BookDetailsPage
from tests.pages.home_page import HomePage


def test_random_book_title_price_consistency(page: Page) -> None:
    """Compare displayed titles and prices for randomly selected books."""
    home_page = HomePage(page)
    details_page = BookDetailsPage(page)

    home_page.open()

    selected_books = home_page.select_random_books()

    for book in selected_books:
        title_link = home_page.get_book_title_link(book)

        homepage_title = title_link.get_attribute("title")
        homepage_price = book.locator(".price_color").inner_text()

        assert homepage_title, "Homepage book title is missing"
        assert homepage_price, "Homepage book price is missing"

        title_link.click()

        expect(details_page.title).to_be_visible()
        expect(details_page.title).to_have_text(homepage_title)

        expect(details_page.price).to_be_visible()
        expect(details_page.price).to_have_text(homepage_price)

        details_page.go_back()
        expect(page).to_have_url(HomePage.URL)
