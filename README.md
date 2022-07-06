# About this project
- Serverless
- Python
- DynamoDB
- ApiGateway
- S3
- SNS
- Lambda

This is a simple project simulating an email subscription to get daily inspiration quotes.

The FE users enter their email and the message to be send
	User can enter information through an API Gateway.
	The request will go to a lambda to retrieve a Qoute from S3.
	In addition it will go to another lambda to subscribe the user

When we save the information of the user (email) we are going to invoke an SNS to notify admins about a subscription of the user.
Another Lambda at a different point in time will grab a different Quote from S3 and send this quote to our subscribers through SendGrid API.
	The Event is trigger by scheduling on CloudWatch and EventBridge.

## Installation Guide
For local test, run

    docker-compose up

At startup localstack runs localstack-init.sh and runs below commands:

Currently the quotes.json file should be placed inside a manually generated S3 bucket for this project to work.

    aws s3api create-bucket \
    --bucket my-bucket \
    --region us-east-1 \
    --endpoint-url http://localhost:4566

Upload Json file

    aws s3 cp quotes.json s3://my-bucket/ --endpoint-url http://localhost:4566

To verify S3 bucket installation

	aws s3 ls s3://my-bucket/ --endpoint-url  http://localhost:4566

To run the healthcheck

	sls invoke -f hello --stage local