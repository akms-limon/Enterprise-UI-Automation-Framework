from urllib.parse import urljoin, urlparse
from playwright.sync_api import Page, expect
from tests.pages.home_page import HomePage


def test_homepage_broken_links(page: Page) -> None:
    home_page = HomePage(page)
    home_page.open()

    # collect all links from homepage
    hrefs = page.locator("a[href]").evaluate_all(
        "(links) => links.map(link => link.getAttribute('href'))"
    )

    broken_links = []
    checked_urls = set()

    for href in hrefs:
        if not href:
            continue

        # Ignore non page links and anchors
        if href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
            continue
        
        # Convert relative URLs to absolute URLs
        url = urljoin(home_page.URL, href)
        parsed_url = urlparse(url)

        if (parsed_url.scheme not in ["http", "https"]):
            continue
        
        # Avoid checking duplicate URLs
        if url in checked_urls:
            continue

        checked_urls.add(url)

        try:
            response = page.request.get(url, timeout=15000)
            if response.status >= 400:
                broken_links.append(
                    f"{url} returned HTTP {response.status}"
                )

        except Exception as error:
            broken_links.append(
                f"{url} could not be reached: {error}"
            )

    assert not broken_links, (
        "Broken links found on homepage:\n"
        + "\n".join(broken_links)
    )