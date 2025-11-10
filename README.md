# pytest-playwright

```
root
├── pyproject.toml                    # Project dependencies & configuration
├── pytest.ini                        # Pytest-specific configuration
├automation_framework/
│├── conftest.py                       # CORE: Fixtures, Hooks, Plugin Config
│├── core/                             # CORE: Reusable framework components
││   ├── __init__.py
││   ├── page_factory.py               # CORE: Dynamic page resolver
││   └── base_page.py                  # CORE: Abstract base page class
│├── config/                           # Configuration management
││   ├── __init__.py
││   ├── settings.py                   # Main settings loader
││   └── environments/
││       ├── base.py                   # Base configuration
││       ├── sit.py                    # SIT environment config
││       └── uat.py                    # UAT environment config
│├── features/                         # BDD Feature files
││  ├── common/                       # Features shared by all customers
││  │   ├── login.feature
││  │   └── navigation.feature
││  └── customer_a/                   # Customer-specific features
││      └── premium_dashboard.feature
│├── steps/                            # Step definitions
││  ├── common/                       # Common step implementations
││  │   ├── __init__.py
││  │   ├── login_steps.py
││  │   └── navigation_steps.py
││  └── customer_a/                   # Customer-specific steps
││      ├── __init__.py
││      └── dashboard_steps.py
│├── web/                              # Page Object Model Structure
││  ├── pages/                        # Common Page abstractions
││  │   ├── __init__.py
││  │   ├── login_page.py             # Common LoginPage ABC/implementation
││  │   └── home_page.py
││  ├── locators/                     # Locator definitions
││  │   ├── common/                   # Common locators
││  │   │   ├── __init__.py
││  │   │   ├── login_locators.py
││  │   │   └── home_locators.py
││  │   └── customer_a/               # Customer-specific locators
││  │       ├── __init__.py
││  │       ├── login_locators.py
││  │       └── dashboard_locators.py
││  └── customers/                    # Concrete customer implementations
││      ├── __init__.py
││      ├── customer_a/
││      │   ├── __init__.py
││      │   ├── login_page.py         # Overrides common LoginPage
││      │   └── dashboard_page.py     # Extends common pages
││      └── customer_b/
││          ├── __init__.py
││          └── login_page.py
│├── helpers/                          # Utility functions
││   ├── __init__.py
││   ├── api_client.py                 # API helpers for test data setup
││   ├── data_generators.py            # Test data generation
││   └── report_utils.py               # Custom reporting utilities
│└── tests/                            # Unit tests for the framework itself
│    ├── __init__.py
│    ├── test_page_factory.py
│    └── test_base_page.py
```

conftest.py is the orchestrator - it sets up the stage for every test

PageFactory is the brain - it makes the multi-tenant magic happen

BasePage is the contract - it ensures consistency across all pages

Settings is the config manager - it handles environment differences cleanly


## Requirements

- Python 3.8 or higher.

## Installation

1. Clone the repository.
2. Navigate to the project's root directory.
3. Create a local venv, if it does not exists.
   ```bash
   python -m venv .venv
   ```
  Activate the local env on terminal -> Windows - .\.venv\Scripts\Activate.ps1

4. Install the dependencies using the following command:

   ```bash
   pip install -e .
   ```
5. Install Playwright:
  ```
  playwright install

  ```

