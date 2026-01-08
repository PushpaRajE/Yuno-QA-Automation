VALID_PAYMENT_MINIMAL = {
    "amount": {
        "value": 100,
        "currency": "USD"
    },
    "workflow": "DIRECT"
}

INVALID_PAYMENT = {
    "amount": {
        "value": -10,
        "currency": "USD"
    },
    "workflow": "DIRECT"
}
