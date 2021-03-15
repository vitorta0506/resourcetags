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
    for volume in ec2.volumes.filter(Filters=[{'Name':'create-time','Values':[date_filter]}]):
      print(volume.id)
      for attachment in volume.attachments:
        print(attachment['InstanceId'])
        for name in ec2.Instance(attachment['InstanceId']).tags:
              try:
                if name['Key'] == ['tag1']:
                      tag = volume.create_tags(
                        DryRun=False,
                        Resources=[volume.id],
                        Tags=[{'Key':['tag1'],'Value':name['Value']}])
              except Exception as e:
                print(e)
                continue                      
              

#loop for tag company

def tag_company():
    print("Loop for TAG company")
    for volume in ec2.volumes.filter(Filters=[{'Name':'create-time','Values':[date_filter]}]):
      print(volume.id)
      for attachment in volume.attachments:
        print(attachment['InstanceId'])
        for name in ec2.Instance(attachment['InstanceId']).tags:
              try:
                if name['Key'] == ['tag2']:
                      tag = volume.create_tags(
                        DryRun=False,
                        Resources=[volume.id],
                        Tags=[{'Key':['tag2'],'Value':name['Value']}])
              except Exception as e:
                print(e)
                continue

#loop for tag application

def tag_application():
    print("Loop for TAG application")
    for volume in ec2.volumes.filter(Filters=[{'Name':'create-time','Values':[date_filter]}]):
      print(volume.id)
      for attachment in volume.attachments:
        print(attachment['InstanceId'])
        for name in ec2.Instance(attachment['InstanceId']).tags:
              try:
                if name['Key'] == ['tag3']:
                      tag = volume.create_tags(
                        DryRun=False,
                        Resources=[volume.id],
                        Tags=[{'Key':['tag3'],'Value':name['Value']}])
              except Exception as e:
                print(e)
                continue

def tag_environment():
    print("Loop for TAG environment")
    for volume in ec2.volumes.filter(Filters=[{'Name':'create-time','Values':[date_filter]}]):
      print(volume.id)
      for attachment in volume.attachments:
        print(attachment['InstanceId'])
        for name in ec2.Instance(attachment['InstanceId']).tags:
              try:
                if name['Key'] == ['tag4']:
                      tag = volume.create_tags(
                        DryRun=False,
                        Resources=[volume.id],
                        Tags=[{'Key':['tag4'],'Value':name['Value']}])
              except Exception as e:
                print(e)
                continue
              

tag_name()
tag_company()
tag_application()
tag_environment()