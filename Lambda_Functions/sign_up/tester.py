import json
from lambda_function import handler

event = {
    "body": json.dumps({
        "email": "test1",
        "password": "test"
    })
}
context = None

response = handler(event, context)

print(response)