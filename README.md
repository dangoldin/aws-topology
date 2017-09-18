# aws-topology
Script to visualize the topology of an AWS environment

The goal is to examine the different services in order to see what instance is set up to talk to what instance and plot these out.

Steps:

- Get all instances, VPCs, Security Groups, ELBs
- Group all instances by ELB
- Find relationship between security groups, vpcs, and instances
