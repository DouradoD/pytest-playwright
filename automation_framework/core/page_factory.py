"""
CORE PAGE FACTORY - Adapted from your working Pages class
"""
import inspect
from importlib import import_module
from pkgutil import walk_packages
from playwright.sync_api import Page
from core.base_page import BasePage


class PageFactory:
    """Load the pages and locators - based on your working code"""

    def __init__(self, page: Page, environment: str, base_url: str, customer: str = "common"):
        self._page = page
        self._environment = environment
        self._base_url = base_url
        self._customer = customer
        self._pages_dict = {}
        self._locators_dict = {}
        self._cache = {}
        
        self.load_pages()

    def load_pages(self):
        """Load all pages and locators using your working approach."""
        pages_dict_ = {}
        locators_dict_ = {}
        
        # Start from the web package
        package = 'web'
        modules_pages = import_module(package)
        
        # Recursively walk through all packages
        for module_info in walk_packages(path=modules_pages.__path__, prefix=f'{modules_pages.__name__}.'):
            try:
                module = import_module(module_info.name)
                print(f"Scanning module: {module_info.name}")
                
                for _, obj in inspect.getmembers(module, lambda m: inspect.isclass(m) and m.__module__ == module_info.name):
                    # Register locators (using mapping_name)
                    if hasattr(obj, 'mapping_name'):
                        key = f"{obj.mapping_name}::{getattr(obj, 'environment', 'common')}"
                        if key not in locators_dict_:
                            locators_dict_[key] = obj
                            print(f"  Found locator: {key}")
                    
                    # Register pages (using page_name)  
                    if hasattr(obj, 'page_name'):
                        key = f"{obj.page_name}::{getattr(obj, 'environment', 'common')}"
                        if key not in pages_dict_:
                            pages_dict_[key] = obj
                            print(f"  Found page: {key}")
                            
            except Exception as e:
                print(f"Error loading module {module_info.name}: {e}")
                continue

        self._pages_dict = pages_dict_
        self._locators_dict = locators_dict_
        
        print(f"\nDiscovery Summary:")
        print(f"Pages found: {list(pages_dict_.keys())}")
        print(f"Locators found: {list(locators_dict_.keys())}")

    def _get_page_instance(self, page_name: str):
        """Get a page instance with injected dependencies."""
        # Priority 1: Environment-specific page
        env_key = f"{page_name}::{self._environment}"
        if env_key in self._pages_dict:
            page_class = self._pages_dict[env_key]
        else:
            # Priority 2: Common page
            common_key = f"{page_name}::common"
            if common_key in self._pages_dict:
                page_class = self._pages_dict[common_key]
            else:
                # Priority 3: Any page with this name
                for key, cls in self._pages_dict.items():
                    if key.startswith(f"{page_name}::"):
                        page_class = cls
                        break
                else:
                    raise PageNotFoundException(
                        f"Page '{page_name}' not found for environment '{self._environment}'. "
                        f"Available: {list(set(k.split('::')[0] for k in self._pages_dict.keys()))}"
                    )

        # Get corresponding locators
        env_locator_key = f"{page_name}::{self._environment}"
        if env_locator_key in self._locators_dict:
            locator_class = self._locators_dict[env_locator_key]
        else:
            common_locator_key = f"{page_name}::common"
            if common_locator_key in self._locators_dict:
                locator_class = self._locators_dict[common_locator_key]
            else:
                for key, cls in self._locators_dict.items():
                    if key.startswith(f"{page_name}::"):
                        locator_class = cls
                        break
                else:
                    raise LocatorNotFoundException(
                        f"Locators for page '{page_name}' not found. "
                        f"Available: {list(set(k.split('::')[0] for k in self._locators_dict.keys()))}"
                    )

        # Create page instance with dependencies
        return page_class(
            page=self._page,
            base_url=self._base_url,
            locators=locator_class()  # Instantiate locators
        )

    def __getattr__(self, page_name: str):
        """Magic method that provides page instances as attributes."""
        if page_name in self._cache:
            return self._cache[page_name]
            
        page_instance = self._get_page_instance(page_name)
        self._cache[page_name] = page_instance
        return page_instance


class PageNotFoundException(Exception):
    pass


class LocatorNotFoundException(Exception):
    pass