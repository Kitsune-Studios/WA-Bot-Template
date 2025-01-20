"""Entrypoint for the Pulumi program."""

from os import getenv

import pulumi
from dotenv import load_dotenv
from pulumi import Config
from pulumi_aws import s3 as aws_s3
from pulumi_gcp import storage as gcp_storage

config = Config()
load_dotenv()
bucket_name = getenv("GCP_BUCKET", "kitsune-bucket")
# chosse between AWS and GCP
if config.get("cloud_provider") == "aws":
    # Create an AWS resource (S3 Bucket)
    bucket = aws_s3.Bucket(bucket_name)
    # Export the DNS name of the bucket
else:
    # Create a GCP resource (Storage Bucket)
    bucket = gcp_storage.Bucket(bucket_name)


# Create a GCP resource (Storage Bucket)

# Export the DNS name of the bucket
pulumi.export(bucket_name, bucket.url)
