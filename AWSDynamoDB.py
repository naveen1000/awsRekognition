import json

import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('WaapChanges')      
    
    '''----- Getting Item -------------
    resp = table.get_item(
            Key={
                'Number' : '7287075568',
            }
        )
                
    if 'Item' in resp:
        print(resp['Item'])'''
    
    ''' ---- Creating Item---------
    post1 = {
        'Number': "7981405016",
        'About': 'Nothing',
        'Profile': 'https://pbs.twimg.com/media/Fg86PI_acAAv-K9.jpg'
    }
    
    table.put_item(Item=post1)'''
    
    table.update_item(
        Key={
                'Number': '7981405016',
            },
        UpdateExpression="set Wapp_Name = :g",
        ExpressionAttributeValues={
                ':g': "Loki Jio"
            },
        ReturnValues="UPDATED_NEW"
        )

        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
