#!/bin/bash

set -e

export AWS_DEFAULT_REGION=us-east-1
export S3_BUCKET=email-subscription-quotes-local

aws s3api create-bucket \
    --bucket $S3_BUCKET \
    --region $AWS_DEFAULT_REGION \
    --endpoint-url http://localhost:4566

aws s3 cp /opt/quotes.json s3://$S3_BUCKET/ --endpoint-url http://localhost:4566