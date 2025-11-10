import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from core.page_factory import PageFactory
from config.settings import get_settings

def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption("--customer", action="store", default="common", 
                    help="Customer variant: common, customer_a, customer_b")
    parser.addoption("--env", action="store", default="uat",
                    help="Execution environment: dev, sit, uat")

@pytest.fixture(scope="session")
def settings(request):
    """Load settings based on environment."""
    env = request.config.getoption("--env")
    return get_settings(env)

@pytest.fixture
def environment(request):
    """Get current environment."""
    return request.config.getoption("--env")

@pytest.fixture
def customer(request):
    """Get current customer variant."""
    return request.config.getoption("--customer")

@pytest.fixture(scope="session")
def playwright_browser(settings, request):
    """ browser creation with full control."""
    headless = getattr(settings, 'headless', True)
    slow_mo = getattr(settings, 'slow_mo', 0)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless,
            slow_mo=slow_mo
        )
        print(f"🚀 BROWSER: Headless={headless}, SlowMo={slow_mo}ms")
        yield browser
        browser.close()

@pytest.fixture
def context(playwright_browser, settings):
    """context creation."""
    context = playwright_browser.new_context(
        viewport=settings.viewport,
        ignore_https_errors=settings.ignore_https_errors,
        base_url=settings.base_url
    )
    yield context
    context.close()

@pytest.fixture
def page(context):
    """page creation."""
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def pages(page, environment, customer, settings) -> PageFactory:
    """
    Alternative PageFactory using browser/context/page.
    """
    return PageFactory(
        page=page, 
        environment=environment,
        customer=customer,
        base_url=settings.base_url
    )