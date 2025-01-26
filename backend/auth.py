"""Module responsible for getting the secret from AWS Secrets Manager."""

from os import getenv

ACCESS_TOKEN = getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = getenv("PHONE_NUMBER_ID")
VERSION = getenv("VERSION")
VERIFY_TOKEN = getenv("VERIFY_TOKEN")
APP_ID = getenv("APP_ID")
NGROK_DOMAIN = getenv("NGROK_DOMAIN")
NGROK_AUTH_TOKEN = getenv("NGROK_AUTH_TOKEN")
