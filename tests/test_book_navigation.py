import random
from urllib.parse import urljoin

from playwright.sync_api import Page, expect

from tests.pages.book_details_page import BookDetailsPage
from tests.pages.home_page import HomePage


def test_random_book_navigation(page: Page) -> None:
    home_page = HomePage(page)
    details_page = BookDetailsPage(page)

    home_page.open()

    # Select five unique books randomly
    books = home_page.book_cards.all()

    assert books, "No books are available on the homepage"

    selected_books = random.sample(books, min(5, len(books)))
    
    for book in selected_books:
        title_link = book.locator("h3 a")

        selected_title = title_link.get_attribute("title")
        href = title_link.get_attribute("href")

        assert selected_title, "Book title is missing"
        assert href, "Book link is missing"

        # Build the expected details page URL
        expected_url = urljoin(HomePage.URL, href)

        # Open the selected book
        title_link.click()

        # Verify the expected details page URL
        expect(page).to_have_url(expected_url)

        # Verify the details page content
        expect(details_page.title).to_be_visible()
        expect(details_page.title).to_have_text(selected_title)
        expect(details_page.book_information).to_be_visible()

        # Return to the homepage
        page.go_back()
        expect(page).to_have_url(HomePage.URL)
