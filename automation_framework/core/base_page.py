"""
CORE BASE PAGE - Foundation for all page objects
"""
from abc import ABC, abstractmethod
from playwright.sync_api import Page, expect

class BasePage(ABC):
    """Abstract base page that all page objects must inherit from."""
    
    def __init__(self, page: Page):
        self.page = page
    
    # Navigation methods
    def navigate_to_url(self, url: str):
        self.page.goto(url, wait_until="networkidle")
    
    def get_current_url(self) -> str:
        return self.page.url
    
    def get_page_title(self) -> str:
        return self.page.title()
    
    def go_back(self):
        self.page.go_back()
    
    def go_forward(self):
        self.page.go_forward()
    
    def reload_page(self):
        self.page.reload()