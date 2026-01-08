Feature: Create Payment

  This feature validates payment creation using Yuno payment APIs
  with DIRECT workflow.

  Scenario: Create payment with minimal required fields
    Given a valid payment payload with minimal fields
    When the payment creation API is called
    Then the payment should be created successfully

  Scenario: Create payment with all possible fields
    Given a valid payment payload with complete details
    When the payment creation API is called
    Then the payment should be created successfully

  Scenario: Create payment with invalid card details
    Given a payment payload with invalid card information
    When the payment creation API is called
    Then the payment creation should fail
