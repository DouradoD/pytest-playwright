Feature: Access the Selenium initial Screen

    @uat
    Scenario: Access the Selenium initial Screen
        When he accesses the URL "https://www.selenium.dev/"
        Then he should see the title "Selenium"