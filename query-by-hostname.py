import boto3
from boto3.dynamodb.conditions import Key
import sys

name_param = sys.argv[1]

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hosts')

response = table.query(
    KeyConditionExpression=Key('name').eq(name_param)
)

items = response['Items']
print(items)