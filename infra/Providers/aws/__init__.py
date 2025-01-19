"""Package to provide resources for AWS.

Here we demonstrate how to selectively import and re-export
modules to create a cleaner API for the user.
"""

from .aws_fargate import create_fargate_service
from .ec2 import create_ec2_instance  # Import specific functions/classes
from .s3 import create_s3_bucket

__all__ = [
    "create_ec2_instance",
    "create_fargate_service",
    "create_s3_bucket",
]  # Re-export the modules
