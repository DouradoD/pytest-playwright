import pytest
from pytest_bdd import scenarios, when, then, parsers, given
from playwright.sync_api import Page, expect

# Import the feature file using correct relative path
scenarios("../features/access_selenium.feature")

@given(parsers.parse('he accesses the URL "{url}"'))
@when(parsers.parse('he accesses the URL "{url}"'))
def navigate_to_url(pages, url: str, page: Page):
    """Navigate to a specific URL."""
        # CORRECT WAY: Check browser type and arguments
    browser = page.context.browser
    browser_type = browser.browser_type.name
    launch_args = getattr(browser, '_launch_options', {})
    is_headless = launch_args.get('headless', True)
    
    print(f"Browser: {browser_type}")
    print(f"Headless mode: {is_headless}")
    print(f"Launch args: {launch_args}")
    # Use the exact page name from the decorator - "selenium_home"
    pages.selenium_home.navigate_to_url(url)

@then(parsers.parse('he should see the title "{expected_title}"'))
def verify_page_title(pages, expected_title: str):
    """Verify the page has the expected title."""
    pages.selenium_home.wait_for_page_load()
    print(f"🔍 Verifying page title is: {expected_title}")
    expect(pages.selenium_home.page).to_have_title(expected_title)

@when(parsers.parse('he clicks on the "{button_name}" button'))
def click_button(pages, button_name: str):
    pages.selenium_home.click_on_about_button(button_name)

@when(parsers.parse('he clicks on the "About Selenium" link'))
def click_about_selenium_link(pages):
    pages.selenium_home.click_on_about_selenium_link()

    