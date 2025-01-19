"""Package to provide resources for AWS.

Here we demonstrate how to selectively import and re-export
modules to create a cleaner API for the user.
"""

from .ec2 import create_ec2_instance  # Import specific functions/classes
from .s3 import create_s3_bucket

__all__ = ["create_ec2_instance", "create_s3_bucket"]  # Explicitly list what to expose
