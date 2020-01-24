import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hosts')

table.update_item(
    Key={
        'name': 'host0',
        'ip': '10.0.2.0'
    },
    UpdateExpression='SET so = :val1',
    ExpressionAttributeValues={
        ':val1': 'conectiva linux'
    }
)