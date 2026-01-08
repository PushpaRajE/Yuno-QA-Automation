from behave import given, when, then


@given("a valid customer payload with mandatory fields")
def step_valid_customer_minimal(context):
    pass


@given("a valid customer payload with complete details")
def step_valid_customer_full(context):
    pass


@given("a customer payload with an existing merchant customer id")
def step_duplicate_customer(context):
    pass


@when("the customer creation API is called")
def step_call_create_customer_api(context):
    pass


@then("the customer should be created successfully")
def step_customer_created_success(context):
    pass


@then("the customer creation should fail with an error")
def step_customer_creation_failed(context):
    pass
