import json
from quotes import config
import uuid
from datetime import datetime


def get_quotes(s3):
    response = s3.get_object(Bucket=config.BUCKET_NAME, Key="quotes.json")
    contents = response["Body"].read().decode("utf-8")
    print(f"S3:::{contents}")
    return contents


def subscribe_user(dynamodb, email):
    item = {
        "userId": str(uuid.uuid4()),
        "email": email,
        "subscriber": True,
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    response = dynamodb.put_item(Item=item)
    print(f"DYNAMODB:::{config.DYNAMODB_TABLE}:::{response}")
    return response
