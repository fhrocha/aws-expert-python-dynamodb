import boto3
from boto3.dynamodb.conditions import Key, Attr
import sys

ip_param = sys.argv[1]

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hosts')

response = table.scan(
    FilterExpression=Attr('ip').eq(ip_param)
)

items = response['Items']
print(items)