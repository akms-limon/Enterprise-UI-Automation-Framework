"""Tests for navigation from the homepage to book details."""

from urllib.parse import urljoin

from playwright.sync_api import Page, expect

from tests.pages.book_details_page import BookDetailsPage
from tests.pages.home_page import HomePage


def test_random_book_navigation(page: Page) -> None:
    """Verify that random books open their matching details pages."""
    home_page = HomePage(page)
    details_page = BookDetailsPage(page)

    home_page.open()

    selected_books = home_page.select_random_books()

    for book in selected_books:
        title_link = home_page.get_book_title_link(book)

        selected_title = title_link.get_attribute("title")
        href = title_link.get_attribute("href")

        assert selected_title, "Book title is missing"
        assert href, "Book link is missing"

        expected_url = urljoin(HomePage.URL, href)

        title_link.click()

        expect(page).to_have_url(expected_url)

        expect(details_page.title).to_be_visible()
        expect(details_page.title).to_have_text(selected_title)
        expect(details_page.book_information).to_be_visible()

        details_page.go_back()
        expect(page).to_have_url(HomePage.URL)
