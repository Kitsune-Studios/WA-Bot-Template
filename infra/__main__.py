"""A Google Cloud Python Pulumi program"""

from os import getenv

import pulumi
from dotenv import load_dotenv
from pulumi_gcp import storage

load_dotenv()
bucket_name = getenv("GCP_BUCKET_NAME", "my-bucket")
# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket(bucket_name, location="US")

# Export the DNS name of the bucket
pulumi.export(bucket_name, bucket.url)
