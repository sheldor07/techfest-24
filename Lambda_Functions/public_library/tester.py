from lambda_function import handler
import json

event = {}
context = None

response = handler(event, context)
print(json.loads(response["body"]))