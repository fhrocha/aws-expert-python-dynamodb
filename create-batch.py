import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hosts')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'name': 'host2',
            'ip': '2.2.2.2',
            'so': 'ubuntu',
            'vms': '0'
        }
    )
    batch.put_item(
        Item={
            'name': 'host3',
            'ip': '3.3.3.3',
            'so': 'windows',
            'vms': '0'
        }
    )
    batch.put_item(
        Item={
            'name': 'host4',
            'ip': '4.4.4.4',
            'so': 'ubuntu',
            'vms': '0'
        }
    )