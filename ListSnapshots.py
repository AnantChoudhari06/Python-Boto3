#!/usr/bin/python
import boto3

boto3 = boto3.session.Session(region_name='ap-northeast-2')
ec2 = boto3.client('ec2')

page_iterator = ec2.get_paginator('describe_snapshots').paginate()

for page in page_iterator:
    for snapshot in page['Snapshots']:
        print(snapshot['SnapshotId'], snapshot['StartTime'])
