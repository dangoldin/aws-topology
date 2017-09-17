#! /usr/bin/env python

import boto3
ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')
elb_client = boto3.client('elb')

# Get instances and extract
# - Name
# - Attached ELB
# - Security Groups
# - VPC
def get_instances():
    return ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# Get Security Groups
# - Name
# - Permissions
def get_security_groups():
    return ec2_client.describe_security_groups()

# Get VPCs
# - Name
# - Permissions
def get_vpcs():
    return ec2_client.describe_vpcs()

# Get ELBs
# - Name
# - Instances
def get_elbs():
    return elb_client.describe_load_balancers()

if __name__ == '__main__':
    instances = get_instances()
    security_groups = get_security_groups()
    vpcs = get_vpcs()
    elbs = get_elbs()
