from numpy.random import randint

def handler(event, context) -> dict:
    return dict(
        statusCode=200, 
        body=dict(
            message="Hello from Lambda",
            array=randint(0,10,(3,3)).tolist()
        )
    )