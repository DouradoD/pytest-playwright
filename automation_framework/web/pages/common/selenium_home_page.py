from playwright.sync_api import Page
from core.base_page import BasePage
from core.decorators import page

@page(name="selenium_home", environment="common")
class SeleniumHomePage(BasePage):
    """Page Object for Selenium Home Page."""
    
    def __init__(self, page: Page, base_url: str, locators):
        super().__init__(page)
        self.locators = locators
        
    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")
    
    
    