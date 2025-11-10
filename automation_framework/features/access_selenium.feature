Feature: Access the Selenium initial Screen

  @uat
  Scenario: Access the Selenium initial Screen
    When he accesses the URL "https://www.selenium.dev/"
    Then he should see the title "Selenium"

  @uat
  Scenario: Access the About page from Selenium initial Screen
    Given he accesses the URL "https://www.selenium.dev/"
    When he clicks on the "About" button
    And he clicks on the "About Selenium" link
    Then he should see the title "About Selenium | Selenium"
