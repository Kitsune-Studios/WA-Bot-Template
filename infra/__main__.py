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
VM_NAME = GCP + "instance_kitsune"
gcp_compute = compute.Instance(
    # Create a GCP resource (Compute Instance)
    name=VM_NAME,
    machine_type="e2-micro",
    zone=LOCATION,
    # Disks are a list of objects, each containing their own disk options
    boot_disk=compute.InstanceBootDiskArgs(
        initialize_params=compute.InstanceBootDiskInitializeParamsArgs(
            image="debian-cloud/debian-9",
        ),
    ),
    # The network interfaces to attach to the instance
    network_interfaces=[
        compute.InstanceNetworkInterfaceArgs(
            network=compute.NetworkArgs(name="default"),
        ),
    ],
    # Non-preemptible instances are free to use, but can be stopped at any time
    scheduling=compute.InstanceSchedulingArgs(preemptible=True),
)

# Create a GCP resource (Storage Bucket)

# Export the DNS name of the bucket
export(BUCKET_NAME, gcp_bucket.url)
export(VM_NAME, gcp_compute.name)
