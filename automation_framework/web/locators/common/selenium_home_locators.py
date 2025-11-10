from dataclasses import dataclass
from core.decorators import locator

@locator(page_name="selenium_home", environment="uat")
@dataclass
class SeleniumHomeLocators:
    about_selenium_link: str = "a[href='/about']"