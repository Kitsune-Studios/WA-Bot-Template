"""Entrypoint for the Pulumi program."""

from os import getenv

import pulumi
from dotenv import load_dotenv
from pulumi import Config

config = Config()
load_dotenv()

# chosse between AWS and GCP
if config.get("cloud_provider") == "aws":
    # Create an AWS resource (S3 Bucket)
    bucket = pulumi.Aws.S3.Bucket("kitsune-bucket")
    # Export the DNS name of the bucket


bucket_name = getenv("GCP_BUCKET", "kitsune-bucket")
# Create a GCP resource (Storage Bucket)

# Export the DNS name of the bucket
pulumi.export(bucket_name, bucket.url)
