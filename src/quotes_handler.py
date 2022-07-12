import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, "quotes"))

import json
from quotes import config
from quotes.repository import aws_repository


def get_quotes(event, context):

    print(f"Incoming::: {event}")

    quotes_json = aws_repository.get_quotes(config.S3_CLIENT)
    print(f"Quotes:::{quotes_json}")

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*"
        },
        "body": quotes_json
    }

    return response
