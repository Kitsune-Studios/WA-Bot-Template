"""Entrypoint for the Pulumi program."""

from os import getenv

from dotenv import load_dotenv
from pulumi import export
from pulumi_gcp import compute, storage

load_dotenv()
GCP = "gcp_"  # Prefix for GCP resources
AWS = "aws_"  # Prefix for AWS resources

LOCATION = getenv("GCP_LOCATION", "us-central1")
BUCKET_NAME = getenv("BUCKET_NAME", "kitsune-bucket")

gcp_bucket = storage.Bucket(GCP + BUCKET_NAME, location=LOCATION)
gcp_compute = compute.Instance(
    GCP + "instance",
    machine_type="n1-standard-1",
    zone="us-central1-a",
)

# Create a GCP resource (Storage Bucket)

# Export the DNS name of the bucket
export(BUCKET_NAME, gcp_bucket.url)
