import random
from playwright.sync_api import Page, expect
from tests.pages.book_details_page import BookDetailsPage
from tests.pages.home_page import HomePage


def test_random_book_title_price_consistency(page: Page) -> None:
    home_page = HomePage(page)
    details_page = BookDetailsPage(page)

    home_page.open()

    books = home_page.book_cards.all()
    assert books, "No books are available on the homepage"

    selected_books = random.sample(books, min(5, len(books)))

    for book in selected_books:
        title_link = book.locator("h3 a")

        homepage_title = title_link.get_attribute("title")
        homepage_price = book.locator(".price_color").inner_text()

        assert homepage_title, "Homepage book title is missing"
        assert homepage_price, "Homepage book price is missing"

        title_link.click()

        expect(details_page.title).to_be_visible()
        expect(details_page.title).to_have_text(homepage_title)

        expect(details_page.price).to_be_visible()
        expect(details_page.price).to_have_text(homepage_price)

        page.go_back()
        expect(page).to_have_url(HomePage.URL)
