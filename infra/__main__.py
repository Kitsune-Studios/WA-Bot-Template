"""An AWS Python Pulumi program."""

import pulumi
from pulumi_aws import ec2, s3

# Get the current stack reference
stack = pulumi.get_stack()
env_vars = pulumi.Config().require_object("env_vars")

# Get the latest Amazon Linux 2 AMI
ami = ec2.get_ami(
    most_recent=True,
    owners=["amazon"],
    filters=[{"name": "name", "values": ["amzn2-ami-hvm-*-x86_64-gp2"]}],
)

# Create a security group
security_group = ec2.SecurityGroup(
    "app-securitygroup",
    description="Enable HTTP access",
    ingress=[
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "tcp",
            "from_port": 22,
            "to_port": 22,
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ],
    egress=[
        {"protocol": "-1", "from_port": 0, "to_port": 0, "cidr_blocks": ["0.0.0.0/0"]},
    ],
)

# User data script for Docker installation and setup
user_data = """#!/bin/bash
yum update -y
yum install -y docker
service docker start
usermod -a -G docker ec2-user
# Add your docker commands here
"""

# Create EC2 instance
instance = ec2.Instance(
    "app-server",
    instance_type="t2.micro",
    vpc_security_group_ids=[security_group.id],
    ami=ami.id,
    user_data=user_data,
    tags={
        "Name": f"app-server-{stack}",
    },
)

# Create an AWS resource (S3 Bucket)
bucket = s3.BucketV2("my-bucket")

# Export the name of the bucket
pulumi.export("bucket_name", bucket.id)

# Export the instance public IP and DNS
pulumi.export("public_ip", instance.public_ip)
pulumi.export("public_dns", instance.public_dns)
pulumi.export("instance_id", instance.id)
