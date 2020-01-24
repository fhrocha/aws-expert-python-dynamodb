import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hosts')

with table.batch_writer() as batch:
    for i in range(50):
        batch.put_item(
            Item={
                'name': 'host' + str(i),
                'ip': '10.0.2.' + str(i),
                'so': 'unknown',
                'vms': 'unknown'
            }
        )