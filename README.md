

# Test locally

## Build Docker Image
docker build -t aws-lambda-image:test .

## Run Docker Image
docker run -p 9000:8080 aws-lambda-image:test

## POST request
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{"""msg""":"""hello"""}"
> {"statusCode": 200, "body": {"message": "Hello from Lambda", "array": [[6, 5, 5], [7, 5, 8], [5, 8, 9]]}}


# Deploy to AWS

- login https://kmatic.awsapps.com/start/

## Elastic Container Registry (ECR)
- create a new repo in ECR
- follow the push commands to push the docker image to ECR
- copy the ui to the docker image in ECR

## Lambda
- create a new lambda function
- select using a docker image
- copy the ui of the docker image from ECR
- deploy and et voila!