import boto3
import json
import logging

from botocore.exceptions import ClientError
from ghapi.all import GhApi


class RepoConfigurer:
    """
    This class is used to create new repos or alter existing ones.  It reads in user-defined config files
    which provide repo parameters.  Repos are either created or their settings are altered according to the
    information contained in these files.
    """

    def __init__(self):
        token = self.get_token()
        self.api = GhApi(token=token)

    def get_token(self):
        """
        Retrieve GitHub token from secrets manager
        """

        secret_name = "GH_TOKEN"
        region_name = "us-east-1"

        session = boto3.session.Session()
        client = session.client(service_name="secretsmanager", region_name=region_name)

        try:
            get_secret_value_response = client.get_secret_value(SecretId=secret_name)

            logging.info("GitHub token successfully fetched")

        except ClientError as e:
            logging.error(f"Failed to fetch GitHub token: {e}")

            raise e

        secret = get_secret_value_response["SecretString"]
        secret = json.loads(secret)

        return secret["GH_TOKEN"]

    def create_repo(self, config_dict):
        """
        Create a repo according to a user-defined config file
        """

        try:
            self.api.repos.create_for_authenticated_user(
                name=config_dict["name"],
                description=config_dict["description"],
                private=config_dict["private"],
                auto_init=config_dict["auto_init"],
            )

            logging.info(f"Successfully created repo {config_dict['name']}")

        except Exception as e:
            logging.error(f"Failed to create repo: {e}")

            raise e

    def alter_repo(self, config_dict):
        ###TO DO###
        """
        Updates an existing repo to reflect information in the corresponding
        user-defined config file
        """

    def update_default_branch(self, config_dict):
        ###TO DO###
        """
        Update the default branch of the repository to the given branch.
        """

    ###ADD MORE CONFIG METHODS - GITIGNORE, CODEOWNERS, ETC.###

    def notify_users(self, config_dict):
        ###TO DO###
        """
        Upon creation/alteration of repo, send a message via SES/SNS to codeowners,
        informing them of changes
        """
