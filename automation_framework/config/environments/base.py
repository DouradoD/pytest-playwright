from dataclasses import dataclass
from typing import Dict

@dataclass
class EnvironmentConfig:
    base_url: str = "https://www.selenium.dev"
    viewport: Dict[str, int] = None
    ignore_https_errors: bool = False
    api_timeout: int = 30000
    headless: bool = False
    slow_mo: int = 100
    
    def __post_init__(self):
        if self.viewport is None:
            self.viewport = {"width": 1920, "height": 1080}

# Base configuration
config = EnvironmentConfig()