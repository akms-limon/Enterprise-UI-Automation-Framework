"""Tests for product image attributes and catalog pagination."""

from playwright.sync_api import Page, expect

from tests.pages.home_page import HomePage


def test_product_images_across_pages(page: Page) -> None:
    """Validate product images while visiting up to five catalog pages."""
    home_page = HomePage(page)
    home_page.open()

    for page_number in range(1, 6):
        print(f"Validating page {page_number}: {page.url}")

        images = home_page.product_images

        expect(images.first).to_be_visible()

        image_count = images.count()
        assert image_count > 0, f"No images found on page {page_number}"

        for image in images.all():
            expect(image).to_be_visible()

            src = image.get_attribute("src")
            alt = image.get_attribute("alt")
            class_name = image.get_attribute("class")

            assert src and src.strip(), "Image src is missing"
            assert alt and alt.strip(), "Image alt text is missing"
            assert class_name and "thumbnail" in class_name.split(), (
                "Image class does not contain 'thumbnail'"
            )

        if page_number == 5:
            print("Reached maximum of 5 pages. Stopping.")
            break

        if not home_page.has_next_page():
            print("No more pages available. Stopping.")
            break

        current_url = page.url
        home_page.go_to_next_page()
        expect(page).not_to_have_url(current_url)
