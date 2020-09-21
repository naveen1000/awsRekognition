import json
import boto3

sns = boto3.resource('sns')
topic = sns.Topic('arn:aws:sns:us-east-1:601147547236:crickNotify')


def lambda_handler(event, context):
    response = topic.publish(
    Message='hello naveen from lamda',
    Subject='string')


import json

def lambda_handler(event, context):
	#1. Parse out query string params
	no = event['queryStringParameters']['no']
	msg = event['queryStringParameters']['msg']


	print('no=' + no)
	print('transactionmsg=' + msg)

	#2. Construct the body of the response object
	transactionResponse = {}
	transactionResponse['transactionId'] = no
	transactionResponse['type'] = msg

	#3. Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(transactionResponse)

	#4. Return the response object
	return responseObject
