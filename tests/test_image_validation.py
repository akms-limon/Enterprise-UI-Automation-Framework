"""Tests for product image attributes and catalog pagination."""

from playwright.sync_api import Page, expect

from tests.pages.home_page import HomePage


def test_product_images_across_pages(page: Page) -> None:
    """Validate product images while visiting up to five catalog pages."""
    home_page = HomePage(page)
    home_page.open()

    for page_number in range(1, 6):
        print(f"Validating page {page_number}: {page.url}")

        images = page.locator("article.product_pod img")

        expect(images.first).to_be_visible()

        image_count = images.count()
        assert image_count > 0, (
            f"No images found on page {page_number}"
        )

        for image in images.all():
            expect(image).to_be_visible()

            src = image.get_attribute("src")
            alt = image.get_attribute("alt")
            class_name = image.get_attribute("class")

            assert src and src.strip(), "Image src is missing"
            assert alt and alt.strip(), "Image alt text is missing"
            assert (
                class_name and "thumbnail" in class_name.split()
            ), "Image class does not contain 'thumbnail'"

        if page_number == 5:
            print("Reached maximum of 5 pages. Stopping.")
            break

        next_button = page.locator("li.next a")

        if not next_button.is_visible() or not next_button.is_enabled():
            print("No more pages available. Stopping.")
            break

        current_url = page.url
        next_button.click()
        expect(page).not_to_have_url(current_url)
