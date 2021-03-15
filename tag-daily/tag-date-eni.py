# set variable AWS_PROFILE= to credentials
import boto3
import os
from datetime import date

#Variáveis das Tag`s

tag1 = 'Name'
tag2 = 'company'
tag3 = 'application'
tag4 = 'environment'


#Conexão com os recursos
ec2 = boto3.resource('ec2', 'us-east-1')
date_filter = date.isoformat(date.today()) + '*'


def tag_name():
    print("Loop for TAG Name")
    for instance in ec2.instances.filter(Filters=[{'Name':'launch-time','Values':[date_filter]}]):
        for eni in instance.network_interfaces:
            print(eni.id)
            for name in instance.tags:
                try:
                    if name['Key'] == ['tag1']:
                        tag = instance.create_tags(
                            DryRun=False,
                            Resources=[eni.id],
                            Tags=[{'Key':['tag1'],'Value':name['Value']}])
                except Exception as e:
                    print(e)
                    continue
                


def tag_company():
    print("Loop for TAG company")
    for instance in ec2.instances.filter(Filters=[{'Name':'launch-time','Values':[date_filter]}]):
        for eni in instance.network_interfaces:
            print(eni.id)
            for name in instance.tags:
                try:
                    if name['Key'] == ['tag2']:
                        tag = instance.create_tags(
                            DryRun=False,
                            Resources=[eni.id],
                            Tags=[{'Key':['tag2'],'Value':name['Value']}])
                except Exception as e:
                    print(e)
                    continue
                    

def tag_application():
    print("Loop for TAG application")
    for instance in ec2.instances.filter(Filters=[{'Name':'launch-time','Values':[date_filter]}]):
        for eni in instance.network_interfaces:
            print(eni.id)
            for name in instance.tags:
                try:
                    if name['Key'] == ['tag3']:
                        tag = instance.create_tags(
                            DryRun=False,
                            Resources=[eni.id],
                            Tags=[{'Key':['tag3'],'Value':name['Value']}])
                except Exception as e:
                    print(e)
                    continue
                    
def tag_environment():
    print("Loop for TAG environment")
    for instance in ec2.instances.filter(Filters=[{'Name':'launch-time','Values':[date_filter]}]):
        for eni in instance.network_interfaces:
            print(eni.id)
            for name in instance.tags:
                try:
                    if name['Key'] == ['tag4']:
                        tag = instance.create_tags(
                            DryRun=False,
                            Resources=[eni.id],
                            Tags=[{'Key':['tag4'],'Value':name['Value']}])
                except Exception as e:
                    print(e)
                    continue
                    
                    
tag_name()
tag_company()
tag_application()
tag_environment()