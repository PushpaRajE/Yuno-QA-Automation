import os

BASE_URL = "https://api-sandbox.y.uno/v1"

HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "public-api-key": os.getenv("PUBLIC_API_KEY", "your_public_key"),
    "private-secret-key": os.getenv("PRIVATE_SECRET_KEY", "your_private_key"),
}
