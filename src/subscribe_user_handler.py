import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, "quotes"))

import json
from quotes import config
from quotes.repository import aws_repository


def subscribe(event, context):
    print(f"EVENT::: {event}")

    data = json.loads(event["body"])
    status_code = 200

    body = {
        "message": "Email subscribed successfully"
    }
    if "email" not in data:
        status_code = 400
        body["message"] = "No field email in request found"

    dynamo_response = aws_repository.subscribe_user(config.DYNAMODB_CLIENT, data["email"])

    if not dynamo_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        status_code = 400
        body["message"] = "Error in DynamoDB"

    response = {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }

    return response
