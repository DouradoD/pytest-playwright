from core.base_page import BasePage
from core.decorators import page

@page(name="selenium_home", environment="common")
class SeleniumHomePage(BasePage):
    """Page Object for Selenium Home Page."""
    
    def __init__(self, page, locators):
        super().__init__(page)
        self.locators = locators
        
    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")
    
    def click_on_about_button(self, button_name: str):
        self.page.get_by_role("button", name=button_name).click()

    def click_on_about_selenium_link(self):
        self.page.locator(self.locators.about_selenium_link).click()
        
    
    
    