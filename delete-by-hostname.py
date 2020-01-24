import boto3
from boto3.dynamodb.conditions import Key
import sys

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hosts')

name_param = sys.argv[1]

response = table.query(
    KeyConditionExpression=Key('name').eq(name_param)
)

items = response['Items']

table.delete_item(
    Key={
        'name': items[0]['name'],
        'ip': items[0]['ip'] 
    }
)