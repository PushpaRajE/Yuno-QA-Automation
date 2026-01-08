from behave import given, when, then
from utils.api_client import APIClient
from utils.config import BASE_URL, HEADERS


@given("a valid customer payload with mandatory fields")
def step_valid_customer_minimal(context):
    context.payload = {
        "merchant_customer_id": "cust_12345",
        "email": "testuser@yuno.com",
        "country": "US"
    }


@given("a valid customer payload with complete details")
def step_valid_customer_full(context):
    context.payload = {
        "merchant_customer_id": "cust_12346",
        "email": "testuser_full@yuno.com",
        "country": "US",
        "first_name": "Test",
        "last_name": "User"
    }


@given("a customer payload with an existing merchant customer id")
def step_duplicate_customer(context):
    context.payload = {
        "merchant_customer_id": "cust_12345",
        "email": "duplicate@yuno.com",
        "country": "US"
    }


@when("the customer creation API is called")
def step_call_create_customer_api(context):
    client = APIClient(BASE_URL, HEADERS)
    context.response = client.post("/customers", context.payload)


@then("the customer should be created successfully")
def step_customer_created_success(context):
    assert context.response.status_code == 201


@then("the customer creation should fail with an error")
def step_customer_creation_failed(context):
    assert context.response.status_code != 201
