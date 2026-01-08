Feature: Cancel Authorized Payment

  Scenario: Cancel authorized payment
    Given an authorized payment exists
    When the cancel API is called
    Then the payment should be cancelled successfully
