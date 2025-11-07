from .base import EnvironmentConfig

# UAT-specific configuration
config = EnvironmentConfig(
    base_url="https://www.selenium.dev",
    headless=False,  # UAT often runs with browser visible
    slow_mo=200,     # Slower execution for demo/debug
    ignore_https_errors=True
)