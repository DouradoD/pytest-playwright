"""
CONFIG SETTINGS - Environment-aware configuration
"""
import os
import importlib
from .environments.base import EnvironmentConfig

def get_settings(env: str = None) -> EnvironmentConfig:
    """Factory function to get environment-specific settings."""
    env = env or os.getenv("TEST_ENV", "uat")
    
    try:
        # Try to load environment-specific config
        env_module = importlib.import_module(f"config.environments.{env}")
        return env_module.config
    except ModuleNotFoundError:
        # Fallback to base config
        from .environments.base import config
        return config