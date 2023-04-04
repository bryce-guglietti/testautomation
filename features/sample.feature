Feature: Search feature

  Scenario: Search for a product
    Given I am on the homepage
    When I click on the login button
    And I login to my account
    When I click on the "Products" button
    And I search for "tshirts"
<<<<<<< HEAD
    When I add 2 "T-Shirts" to cart
=======
    When I add 2 T-Shirts to cart
>>>>>>> efd72d77a1aec2375410546ccb6c3e78c4b0bb41
    When I click on the Cart button
    When I delete an item
    And I click on the Checkout button
    When I click on the Place Order button
    And I fill out the credit card form
<<<<<<< HEAD
    Then I click on the invoice button
=======
    Then I click on the invoice button
>>>>>>> efd72d77a1aec2375410546ccb6c3e78c4b0bb41
