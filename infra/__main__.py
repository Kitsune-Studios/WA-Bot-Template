"""Entrypoint for the Pulumi program."""

from os import getenv

from dotenv import load_dotenv
from pulumi import export
from pulumi_gcp import compute, storage

load_dotenv()
GCP = "gcp_"  # Prefix for GCP resources
AWS = "aws_"  # Prefix for AWS resources
LOCATION = getenv("GCP_LOCATION", "us-east1")

BUCKET_NAME = getenv("BUCKET_NAME", "kitsune-bucket")

gcp_bucket = storage.Bucket(GCP + BUCKET_NAME, location="US")
gcp_compute = compute.Instance(
    GCP + "instance",
    machine_type="e2-micro",
    zone=LOCATION,
    boot_disk=compute.InstanceBootDiskArgs(
        initialize_params=compute.InstanceBootDiskInitializeParamsArgs(
            image="debian-cloud/debian-9",
        ),
    ),
    network_interfaces=[
        compute.InstanceNetworkInterfaceArgs(
            network=compute.NetworkArgs(name="default"),
        ),
    ],
)

# Create a GCP resource (Storage Bucket)

# Export the DNS name of the bucket
export(BUCKET_NAME, gcp_bucket.url)
