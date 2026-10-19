import pytest


@pytest.fixture
def website_url() -> str:
    return "https://books.toscrape.com/index.html"
