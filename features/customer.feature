Feature: Create Customer

  This feature validates customer creation using Yuno APIs.
  Customer creation is required before initiating checkout and payments.

  Scenario: Create customer with minimal required fields
    Given a valid customer payload with mandatory fields
    When the customer creation API is called
    Then the customer should be created successfully

  Scenario: Create customer with all possible fields
    Given a valid customer payload with complete details
    When the customer creation API is called
    Then the customer should be created successfully

  Scenario: Create customer with duplicate merchant customer id
    Given a customer payload with an existing merchant customer id
    When the customer creation API is called
    Then the customer creation should fail with an error
