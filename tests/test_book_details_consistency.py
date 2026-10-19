import random

from playwright.sync_api import Page, expect

from tests.pages.book_details_page import BookDetailsPage
from tests.pages.home_page import HomePage


def test_random_book_title_price_consistency(page: Page) -> None:
    home_page = HomePage(page)
    details_page = BookDetailsPage(page)

    home_page.open()

    # Collect all available books
    books = home_page.book_cards.all()
    assert books, "No books are available on the homepage"

    # Select up to five unique books randomly
    selected_books = random.sample(books, min(5, len(books)))

    for book in selected_books:
        title_link = book.locator("h3 a")

        # Capture homepage title and price
        homepage_title = title_link.get_attribute("title")
        homepage_price = book.locator(".price_color").inner_text()

        assert homepage_title, "Homepage book title is missing"
        assert homepage_price, "Homepage book price is missing"

        # Open the book details page
        title_link.click()

        # Compare homepage title with details page H1
        expect(details_page.title).to_be_visible()
        expect(details_page.title).to_have_text(homepage_title)

        # Compare homepage price with details page price
        expect(details_page.price).to_be_visible()
        expect(details_page.price).to_have_text(homepage_price)

        # Return to homepage
        page.go_back()
        expect(page).to_have_url(HomePage.URL)
