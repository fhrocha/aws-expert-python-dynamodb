import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hosts')

response = table.get_item(
   Key={
        'name': 'host0',
        'ip': '10.0.2.0'
    }
)

item = response['Item']
name = item['name']

print(item)
print("Hello, {}" .format(name))