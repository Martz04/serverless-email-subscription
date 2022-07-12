import os
import boto3


REGION_NAME = os.environ.get("REGION_NAME")
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE")

if 'LOCALSTACK_HOSTNAME' in os.environ:
        endpoint_url = 'http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME']
        print("LOCAL ENVIRONMENT:::", endpoint_url)
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url=endpoint_url,
            region_name=REGION_NAME
        )
        DYNAMODB_CLIENT = dynamodb.Table(DYNAMODB_TABLE)
        S3_CLIENT = boto3.client("s3", endpoint_url=endpoint_url)
        BUCKET_NAME = "email-subscription-quotes-local"

else:
    dynamodb = boto3.resource('dynamodb', region_name=str(os.environ["REGION_NAME"]))
    DYNAMODB_CLIENT = dynamodb.Table(DYNAMODB_TABLE)
    S3_CLIENT = boto3.client("s3")
    BUCKET_NAME = os.environ.get("BUCKET_NAME")
