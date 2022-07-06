#!/bin/bash

set -e

export AWS_DEFAULT_REGION=us-west-1

aws s3api create-bucket \
    --bucket my-bucket \
    --region us-east-1 \
    --endpoint-url http://localhost:4566

aws s3 cp /opt/quotes.json s3://my-bucket/ --endpoint-url http://localhost:4566