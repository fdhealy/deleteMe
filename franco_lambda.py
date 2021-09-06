from __future__ import print_function
import boto3
import json
import datetime
dt = datetime.datetime


def lambda_handler(event, context): 
    dt = datetime.datetime
    now = dt.now()

    timeLeft = dt(year = 2021, month = 6, day = 13) - dt(year=now.year, month=now.month, day=now.day)
    ds = timeLeft.days*24*60*60*10^9
    print (ds+365*24*60*60*10^9)

    return ds+365*24*60*60*10^9

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
    operation = event["potato"]
    mahinfo = event["steak"]
    dynamo = boto3.resource("dynamodb")
    table = dynamo.Table("hellonames")

    operations = {
        "create": lambda x: table.put_item(**x),
        "read": lambda x: table.get_item(**x),
        "update": lambda x: table.update_item(**x),
        "delete": lambda x: table.delete_item(**x),
        "list": lambda x: table.scan(**x),
        "echo": lambda x: x,
        "ping": lambda x: "pong",
    }
    
    
    if operation in operations:
        print("operation = ", operation)
        
        # TODO: Use try catch, handle response code != 200
        return operations[operation](mahinfo)
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))
