from behave import given, when, then


@given("a valid payment payload with minimal fields")
def step_payment_minimal(context):
    pass


@given("a valid payment payload with complete details")
def step_payment_full(context):
    pass


@given("a payment payload with invalid card information")
def step_payment_invalid(context):
    pass


@when("the payment creation API is called")
def step_call_payment_api(context):
    pass


@then("the payment should be created successfully")
def step_payment_success(context):
    pass


@then("the payment creation should fail")
def step_payment_fail(context):
    pass
