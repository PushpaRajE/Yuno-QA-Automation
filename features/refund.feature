Feature: Refund Payment

  Scenario: Refund captured payment successfully
    Given a captured payment exists
    When the refund API is called
    Then the payment should be refunded successfully
