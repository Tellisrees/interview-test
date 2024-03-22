import boto3
import json
import logging

from botocore.exceptions import ClientError
from ghapi.all import GhApi


class RepoAuditor:
    ###TO DO###
    """
    This class is used to audit repos and ensure that they adhere to organisation-wide standards and
    security best practices.
    """
