from boto3 import resource

dynamodb = resource('dynamodb')
database = dynamodb.Table('hosts')

last_evaluated_key = None

while True:
    if last_evaluated_key:
        response = database.scan(ExclusiveStartKey=last_evaluated_key)
    else: 
        response = database.scan()

    last_evaluated_key = response.get('LastEvaluatedKey')
    items = response['Items']
    print (items)
    if not last_evaluated_key:
        break