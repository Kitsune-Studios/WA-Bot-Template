"""Entrypoint for the Pulumi program."""

from os import getenv

from dotenv import load_dotenv
from pulumi import Config, export
from pulumi_aws import s3 as aws_s3
from pulumi_gcp import storage as gcp_storage

GCP = "gcp_"
AWS = "aws_"
config = Config()
config.require("location")
load_dotenv()
LOCATION = getenv("GCP_LOCATION", "us-central1")
BUCKET_NAME = getenv("BUCKET_NAME", "kitsune-bucket")
gcp_bucket = gcp_storage.Bucket(GCP + BUCKET_NAME, location=LOCATION)
# chosse between AWS and GCP
aws_bucket = aws_s3.BucketV2(AWS + BUCKET_NAME)
# Create a GCP resource (Storage Bucket)

# Export the DNS name of the bucket
export(BUCKET_NAME, gcp_bucket.url)
