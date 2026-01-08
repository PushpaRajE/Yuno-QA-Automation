Feature: Payment Authorization

  This feature validates authorization flow for card payments.
  Authorization blocks the amount without capturing it.

  Scenario: Authorize payment successfully
    Given a valid authorization payment payload
    When the authorization API is called
    Then the payment should be authorized successfully

  Scenario: Authorization with invalid card details
    Given an authorization payload with invalid card details
    When the authorization API is called
    Then the authorization should fail
