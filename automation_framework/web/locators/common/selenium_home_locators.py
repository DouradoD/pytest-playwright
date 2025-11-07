from dataclasses import dataclass
from core.decorators import locator

@locator(page_name="selenium_home", environment="common")
@dataclass
class SeleniumHomeLocators:
    # Using simple locators for the demo
    main_header: str = "css=h1"
    documentation_link: str = "css=[href='/documentation']"