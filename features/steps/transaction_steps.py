from behave import given, when, then


@given("a valid authorization payment payload")
def step_valid_authorization(context):
    pass


@given("an authorization payload with invalid card details")
def step_invalid_authorization(context):
    pass


@when("the authorization API is called")
def step_call_authorization(context):
    pass


@then("the payment should be authorized successfully")
def step_authorized(context):
    pass


@then("the authorization should fail")
def step_authorization_fail(context):
    pass


@given("an authorized payment exists")
def step_authorized_payment_exists(context):
    pass


@when("the capture API is called")
def step_call_capture(context):
    pass


@then("the payment should be captured successfully")
def step_captured(context):
    pass


@when("the cancel API is called")
def step_call_cancel(context):
    pass


@then("the payment should be cancelled successfully")
def step_cancelled(context):
    pass


@given("a captured payment exists")
def step_captured_payment_exists(context):
    pass


@when("the refund API is called")
def step_call_refund(context):
    pass


@then("the payment should be refunded successfully")
def step_refunded(context):
    pass
