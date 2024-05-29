

# Test locally

## Build Docker Image
build -t aws-lambda-image:test .

## Run Docker Image
docker run -p 9000:8080 aws-lambda-image:test

## POST request
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{"""msg""":"""hello"""}"
> {"statusCode": 200, "body": {"message": "Hello from Lambda", "array": [[6, 5, 5], [7, 5, 8], [5, 8, 9]]}}