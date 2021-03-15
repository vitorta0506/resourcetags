import boto3
import botocore
from datetime import date
#Variáveis das Tag`s

tag1 = 'Name'
tag2 = 'environment'
tag3 = 'company'
tag4 = 'application'


#Conexão com os recursos
ec2 = boto3.resource('ec2', 'us-east-1')
client = boto3.client('ec2', 'us-east-1')
date_filter = date.isoformat(date.today()) + '*'
snapshot = client.describe_snapshots(OwnerIds=['self'],Filters=[{'Name':'start-time', 'Values':[date_filter]}])


def tag_name():
     print("Loop for TAG Name")
     for snap in snapshot['Snapshots']:
          print(snap['SnapshotId'])
          try:
               volume = client.describe_volumes(VolumeIds=[snap['VolumeId']])
          except Exception as e:
               print(e)
               continue
          for vvolume in volume['Volumes']:
               for name in vvolume['Tags']:
                    try:
                         if name['Key'] == ['tag1']:
                              tag = client.create_tags(
                                   DryRun=False,
                                   Resources=[snap['SnapshotId']],
                                   Tags=[{'Key':['tag1'],'Value':name['Value']}])
                    except Exception as e:
                         print(e)
                         continue                              
                         
            
def tag_environment():
     print("Loop for TAG environment")
     for snap in snapshot['Snapshots']:
          print(snap['SnapshotId'])
          try:
               volume = client.describe_volumes(VolumeIds=[snap['VolumeId']])
          except Exception as e:
               print(e)
               continue
          for vvolume in volume['Volumes']:
               for name in vvolume['Tags']:
                    try:
                         if name['Key'] == ['tag2']:
                              tag = client.create_tags(
                                   DryRun=False,
                                   Resources=[snap['SnapshotId']],
                                   Tags=[{'Key':['tag2'],'Value':name['Value']}])
                    except Exception as e:
                         print(e)
                         continue
                         
def tag_company():
     print("Loop for TAG company")
     for snap in snapshot['Snapshots']:
          print(snap['SnapshotId'])
          try:
               volume = client.describe_volumes(VolumeIds=[snap['VolumeId']])
          except Exception as e:
               print(e)
               continue
          for vvolume in volume['Volumes']:
               for name in vvolume['Tags']:
                    try:
                         if name['Key'] == ['tag3']:
                              tag = client.create_tags(
                                   DryRun=False,
                                   Resources=[snap['SnapshotId']],
                                   Tags=[{'Key':['tag3'],'Value':name['Value']}])
                    except Exception as e:
                         print(e)
                         continue

def tag_application():
     print("Loop for TAG application")
     for snap in snapshot['Snapshots']:
          print(snap['SnapshotId'])
          try:
               volume = client.describe_volumes(VolumeIds=[snap['VolumeId']])
          except Exception as e:
               print(e)
               continue
          for vvolume in volume['Volumes']:
               for name in vvolume['Tags']:
                    try:
                         if name['Key'] == ['tag4']:
                              tag = client.create_tags(
                                   DryRun=False,
                                   Resources=[snap['SnapshotId']],
                                   Tags=[{'Key':['tag4'],'Value':name['Value']}])
                    except Exception as e:
                         print(e)
                         continue

                         
tag_name()
tag_environment()
tag_company()
tag_application()