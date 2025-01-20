"""Entrypoint for the Pulumi program."""

from os import getenv

import pulumi
from dotenv import load_dotenv
from pulumi import Config
from pulumi_gcp import storage as gcp_storage

config = Config()
load_dotenv()
LOCATION = getenv("GCP_LOCATION", "us-central1")
BUCKET_NAME = getenv("GCP_BUCKET", "kitsune-bucket")
bucket = gcp_storage.Bucket(BUCKET_NAME, location=LOCATION)
# chosse between AWS and GCP

# Create a GCP resource (Storage Bucket)

# Export the DNS name of the bucket
pulumi.export(BUCKET_NAME, bucket.url)
