import boto3
region = 'us-east-1'
instances = ['i-008819fe56a631604']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))

import boto3
region = 'us-east-1'
#instances = ['i-04d74c59459c18a43']
#ec2 = boto3.client('ec2', region_name=region)
#res = ec2.start_instances(InstanceIds=instances)
#print(res)
ec2  = boto3.resource('ec2')
instance = ec2.Instance('i-04d74c59459c18a43')

print(instance.public_ip_address)
