import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hosts')

table.put_item(
   Item={
        'name': 'host1',
        'ip': '3.187.222.12',
        'vms': '10',
        'so': 'linux',
    }
)