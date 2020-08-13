import json
import boto3

cloudwatch = boto3.client('logs')

def detect(event, context):
    
    response = cloudwatch.get_log_events(
        logGroupName='spot_teste',
        time=111,
    )

    print(response)