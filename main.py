import logging
import yaml

from pathlib import Path
from ukhsa_github import RepoConfigurer


logging.basicConfig(level=logging.INFO)


def main():

    repo_configurer = RepoConfigurer()

    # Produce a list of all config file paths
    all_config_files_path = Path(__file__).parent / "config_files"
    config_files_dirs_list = [
        entry for entry in all_config_files_path.iterdir() if entry.is_dir()
    ]

    # Create repo for each config file
    for config_file_dir in config_files_dirs_list:
        config_file = config_file_dir / "repo_config.yml"

        with open(str(config_file), "r") as file:
            config_dict = yaml.safe_load(file)

        repo_configurer.create_repo(config_dict)


if __name__ == "__main__":
    main()
