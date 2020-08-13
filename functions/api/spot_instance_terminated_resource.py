import json
import boto3

def detect(event, context):
    client = boto3.client('autoscaling')
    
    instance = boto3.client('ec2')
    
    taginstance = instance.describe_tags(
        Filters=[
        {
            'Name': 'resource-id',
            'Values': [
                event["detail"]["instance-id"],
            ],
        },
    ],
        )
    
    print(taginstance['Tags'][0]['Value'])
    
    response = client.detach_instances(
    InstanceIds=[
        event["detail"]["instance-id"],
    ],
    AutoScalingGroupName=taginstance['Tags'][0]['Value'],
    ShouldDecrementDesiredCapacity=False
)


    print(response)
