from __future__ import print_function
import boto3
import json


# dynamo = boto3.resource('dynamodb')
# table = dynamo.Table('hellonames')
# def update():
#     dynamo.update_item(
#         TableName='hellonames',
#             Key={
#                 'user': {
#                     'S': 'newUser',
#                 },
#             }
#     )
def handler(event, context):
  print('Loading function')
    '''Provide an event that contains the following keys:
      - operation: one of the operations in the operations dict below
      - tableName: required for operations that interact with DynamoDB
      - payload: a parameter to pass to the operation being performed
    '''
    #print("Received event: " + json.dumps(event, indent=2))
    operation = event['operation']
    dynamo = boto3.resource('dynamodb').Table(event['hellonames'])
    operations = {
        'create': lambda x: dynamo.put_item(**x),
        'read': lambda x: dynamo.get_item(**x),
        'update': dynamo.update_item({
          TableName='hellonames',
	        Key={
		        'user': {
			      'S': 'newUser',
		        },
	        }
          }),
        'delete': lambda x: dynamo.delete_item(**x),
        'list': lambda x: dynamo.scan(**x),
        'echo': lambda x: x,
        'ping': lambda x: 'pong'
    }
    if operation in operations:
        return operations[operation]()
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))







Send a message to franco.healy





