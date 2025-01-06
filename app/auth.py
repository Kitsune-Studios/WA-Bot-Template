import boto3
from botocore.exceptions import ClientError
import json

## There needs to be a secret created in the AWS account with the values obtained from Facebook Business Platform


def get_secret(secret_name: str | None = None, region_name: str = "us-east-1"):

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response["SecretString"]

    return json.loads(secret)


# Change name to the correspondent secret from AWS.
# Needs to have AWS credentials to access the secret.
secret_name = "secret_name"

wa_credentials = get_secret(secret_name)

ACCESS_TOKEN = wa_credentials["ACCESS_TOKEN"]
PHONE_NUMBER_ID = wa_credentials["PHONE_NUMBER_ID"]
VERSION = wa_credentials["VERSION"]
VERIFY_TOKEN = wa_credentials["VERIFY_TOKEN"]
APP_ID = wa_credentials["APP_ID"]
NGROK_DOMAIN = wa_credentials["NGROK_DOMAIN"]
NGROK_AUTH_TOKEN = wa_credentials["NGROK_AUTH_TOKEN"]
