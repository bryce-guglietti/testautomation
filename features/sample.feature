Feature: Search feature

  Scenario: Search for a product
    Given I am on the homepage
    When I click on the login button
      And I login to my account
    When I click on the "Products" button
      And I search for "tshirts"
    When I add 2 "T-Shirts" to cart
      And I click on the Cart button
      And I delete an item
    When I click on the Checkout button
      And I click on the Place Order button
      And I fill out the credit card form
    Then I click on the invoice button
