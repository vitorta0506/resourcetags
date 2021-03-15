from __future__ import print_function
from datetime import datetime, timedelta, timezone
from boto3 import client as boto_client
import boto3
import os
from datetime import date
client = boto3.client('docdb', 'us-east-1')
date_filter = date.isoformat(date.today()) + '*'
cluster_docdb = [ cluster_docdb['DBClusterIdentifier'] for cluster_docdb  in  client.describe_db_clusters()['DBClusters'] ]

RETENTION_DAYS = int(os.environ.get('RETENTION_DAYS', 1))

#DATE_SNAP = date_filter
DATE_SNAP = (datetime.utcnow() - timedelta(days=RETENTION_DAYS)).replace(tzinfo=timezone.utc)

def tag_manual():
    for db_cluster_id in cluster_docdb:
        arn = "arn:aws:rds:us-east-1:461150121833:cluster:" + db_cluster_id
        ltag = client.list_tags_for_resource(ResourceName = str(arn))['TagList']
        for snap in client.describe_db_cluster_snapshots(SnapshotType='manual',DBClusterIdentifier=db_cluster_id)['DBClusterSnapshots']:
            if snap['SnapshotCreateTime'] >= DATE_SNAP:
                for tagging in ltag:
                    try:
                        response = client.add_tags_to_resource(ResourceName=snap['DBClusterSnapshotArn'],Tags=[{'Key':(tagging['Key']),'Value':(tagging['Value'])}])
                    except Exception as e:
                        print(e)
                        continue
                    print(snap['DBClusterSnapshotArn'])
                    
                    
def tag_auto():
    for db_cluster_id in cluster_docdb:
        arn = "arn:aws:rds:us-east-1:461150121833:cluster:" + db_cluster_id
        ltag = client.list_tags_for_resource(ResourceName = str(arn))['TagList']
        for snap in client.describe_db_cluster_snapshots(DBClusterIdentifier=db_cluster_id)['DBClusterSnapshots']:
            if snap['SnapshotCreateTime'] >= DATE_SNAP:
                for tagging in ltag:
                    try:
                        response = client.add_tags_to_resource(ResourceName=snap['DBClusterSnapshotArn'],Tags=[{'Key':(tagging['Key']),'Value':(tagging['Value'])}])
                    except Exception as e:
                        print(e)
                        continue
                    print(snap['DBClusterSnapshotArn'])
                    
            
tag_manual()
tag_auto()
