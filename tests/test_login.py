from playwright.sync_api import Page, expect


def test_login_page_navigation(page: Page) -> None:
    page.goto("https://quotes.toscrape.com/")

    # Verify homepage loads successfully
    expect(page).to_have_url("https://quotes.toscrape.com/")

    # Locate and click the Login link
    login_link = page.get_by_role("link", name="Login")
    expect(login_link).to_be_visible()
    expect(login_link).to_be_enabled()
    login_link.click()

    # Verify login page loads successfully
    expect(page).to_have_url("https://quotes.toscrape.com/login")
    expect(page.locator("input[name='username']")).to_be_visible()
    expect(page.locator("input[name='password']")).to_be_visible()



def test_login_and_logout_link(page: Page) -> None:
    page.goto("https://quotes.toscrape.com/")

    # Open the login page
    page.get_by_role("link", name="Login").click()

    # Enter credentials
    page.locator("input[name='username']").press_sequentially("test_user")
    page.locator("input[name='password']").press_sequentially("test_password")

    # Submit the login form
    page.locator("input[type='submit']").click()

    # Verify successful login
    logout_link = page.get_by_role("link", name="Logout")
    expect(logout_link).to_be_visible()
    expect(logout_link).to_be_enabled()
