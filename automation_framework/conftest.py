import pytest
from playwright.sync_api import Page
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
def browser_type_launch_args(browser_type_launch_args, settings, request):
    """
    CORRECT FIXTURE: Override browser launch arguments.
    This is the correct fixture name for pytest-playwright.
    """
    # Use --headed flag or settings
    if request.config.getoption("--headed"):
        headless = False
        print("🚀 BROWSER: Headed mode (--headed flag detected)")
    else:
        headless = settings.headless
        print(f"🚀 BROWSER: Headless mode from settings: {headless}")
    
    launch_args = {
        **browser_type_launch_args,
        "headless": headless,
    }
    
    # Add slow_mo for visual debugging in headed mode
    if not headless and hasattr(settings, 'slow_mo') and settings.slow_mo > 0:
        launch_args["slow_mo"] = settings.slow_mo
        print(f"🚀 BROWSER: Slow motion: {settings.slow_mo}ms")
    
    print(f"🚀 BROWSER: Final launch args: {launch_args}")
    return launch_args

@pytest.fixture
def pages(page: Page, environment, customer, settings) -> PageFactory:
    """
    MAIN FIXTURE: Injects PageFactory with environment context.
    """
    page_factory = PageFactory(
        page=page, 
        environment=environment,
        customer=customer,
        base_url=settings.base_url
    )
    
    return page_factory

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, settings):
    """Configure browser context with global settings."""
    return {
        **browser_context_args,
        "viewport": settings.viewport,
        "ignore_https_errors": settings.ignore_https_errors,
        "base_url": settings.base_url
    }