import boto3
import os
from datetime import date
ec2 = boto3.resource('ec2', 'us-east-1')
client = boto3.client('elb', 'us-east-1')
eni = boto3.client('ec2', 'us-east-1')
responselb = client.describe_load_balancers()
responseeni = eni.describe_network_interfaces()


for elbname in responselb['LoadBalancerDescriptions']:
    elb_name = elbname['LoadBalancerName']
    try:
        elb_idinst = elbname['Instances'][0]['InstanceId']
        
    except Exception as e:
        print(e)
        continue
    
    
    
    for enidesc in responseeni['NetworkInterfaces']:
        desc_eni = enidesc['Description']
        id_eni = enidesc['NetworkInterfaceId']
              
        if (desc_eni[4:]) == (elb_name):
            desctag = eni.describe_tags(DryRun=False,Filters=[{'Name' : 'resource-type','Values' : ['instance']},{'Name' : 'resource-id','Values' : [elb_idinst]}])
            tagg = desctag['Tags']
            for tagging in tagg:
                try:
                    response = eni.create_tags(DryRun=False,Resources=[id_eni],Tags=[{'Key':(tagging['Key']),'Value':(tagging['Value'])}])
                except Exception as e:
                    print(e)
                    continue
                print(id_eni)
                print(elb_name)
               
exit()                
