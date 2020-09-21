import boto3
region = 'us-east-1'
instances = ['i-0db74a6c22a736202']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))


import boto3
region = 'us-east-1'
instances = ['i-0db74a6c22a736202']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))


return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
https://od6u1m3sxb.execute-api.us-east-1.amazonaws.com/default/ubuntuStart
