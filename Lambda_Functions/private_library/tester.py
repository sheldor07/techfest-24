from lambda_function import handler
import json

event = {"body": json.dumps({"token": "8dbb50fe6974e5e3eb574b7f0b3b15defd3bfbf812db9140f461b2d63f406bf94d66c7c2a29ad3459a60b62c96cc631d723d5d5593942efa7ee0c0d80a31c9d051193d2980d28a332ad3cfefd01ec3924016cd4a125b0a6a99fa0b6dd9243fa12d09fffea776aeb5240ae16d6abce77131fc00533e382c6c90ea1eb4c6b650"})}
context = None

response = handler(event, context)
print(json.loads(response["body"]))