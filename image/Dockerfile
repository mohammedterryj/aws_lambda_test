FROM amazon/aws-lambda-python:3.8

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

COPY src/* ${LAMBDA_TASK_ROOT}

CMD [ "main.handler" ]