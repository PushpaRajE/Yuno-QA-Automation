Feature: Capture Authorized Payment

    Scenario: Capture authorized payment successfully
    Given an authorized payment exists
    When the capture API is called
    Then the payment should be captured successfully
