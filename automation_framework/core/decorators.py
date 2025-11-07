"""
CORE DECORATORS - Using your existing attribute names for compatibility
"""
def page(name: str, environment: str = "common"):
    """
    Decorator to register a page class - using your existing attribute names.
    """
    def cls_decorator(cls):
        cls.page_name = name  # Using your existing attribute name
        cls.environment = environment
        return cls
    return cls_decorator


def locator(page_name: str, environment: str = "common"):
    """
    Decorator to register a locator class - using mapping_name for compatibility.
    """
    def cls_decorator(cls):
        cls.mapping_name = page_name  # Using your existing attribute name
        cls.environment = environment
        return cls
    return cls_decorator