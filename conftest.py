"""Shared pytest fixtures for browser setup."""

import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Allow browser contexts to load pages with certificate warnings."""
    return {
        **browser_context_args,
        "ignore_https_errors": True,
    }
