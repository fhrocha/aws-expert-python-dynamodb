import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='hosts',
    KeySchema=[
        {
            'AttributeName': 'name', 
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'ip', 
            'KeyType': 'RANGE'
        }
    ], 
    AttributeDefinitions=[
        {
            'AttributeName': 'name', 
            'AttributeType': 'S'
        }, 
        {
            'AttributeName': 'ip', 
            'AttributeType': 'S'
        }, 
    ], 
    ProvisionedThroughput={
        'ReadCapacityUnits': 1, 
        'WriteCapacityUnits': 1
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='hosts')
print(table.item_count)