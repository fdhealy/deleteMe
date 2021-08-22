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

    print("Received event: " + json.dumps(event, indent=2))
    operation = event["operation"]
    dynamo = boto3.resource("dynamodb")
    table = dynamo.Table("hellonames")

    operations = {
        "create": lambda x: dynamo.put_item(**x),
        "read": lambda x: dynamo.get_item(**x),
        "update": table.update_item(
            Key={
                "user": "newUser",
            },
        ),
        "delete": lambda x: dynamo.delete_item(**x),
        "list": lambda x: dynamo.scan(**x),
        "echo": lambda x: x,
        "ping": lambda x: "pong",
    }
    if operation in operations:
        print("operation = ", operation)
        return operations[operation]()
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))
