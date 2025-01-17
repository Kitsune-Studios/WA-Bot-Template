"""A Google Cloud Python Pulumi program"""

from os import getenv

import pulumi
from dotenv import load_dotenv
from pulumi import Config
from pulumi_docker import Image
from pulumi_gcp import cloudrun, storage
from pulumi_gcp.config import project as gcp_project

config = Config()
project = gcp_project.get()
load_dotenv()
bucket_name = getenv("GCP_BUCKET", "kitsune-bucket")
# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket(bucket_name, location="US")

# Create Docker image from local Dockerfile
image = Image("kitsune-image", build=pulumi.DockerBuild(context="app"))

# Create a GCP resource (Cloud Run Service)
cloud_run = cloudrun.Service(
    "kitsune-service",
    location=Config("gcp").require("region"),
    template=cloudrun.ServiceTemplateArgs(
        spec=cloudrun.ServiceTemplateSpecArgs(
            containers=[
                cloudrun.ServiceTemplateSpecContainerArgs(
                    image="gcr.io/cloudrun/hello",
                    resources=cloudrun.ServiceTemplateSpecContainerResourcesArgs(
                        limits={"cpu": "1", "memory": "1Gi"},
                    ),
                )
            ],
        ),
    ),
    traffics=[cloudrun.ServiceTrafficArgs(latest_revision=True, percent=100)],
)

# Export the DNS name of the bucket
pulumi.export(bucket_name, bucket.url)
pulumi.export("cloud_run_url", cloud_run.statuses[0].url)
