Feature: Search feature

  Scenario: Search for a product
    Given I am on the homepage
    When I click on the "Products" button
    And I search for "tshirts"
    Then I should see a list of tshirts