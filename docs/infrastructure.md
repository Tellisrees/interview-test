# Infrastructure

![](infrastructure.drawio)

- Repository contains builspec.yml file that is triggered by CodeBuild following a successful merge into main from another branch
- CodeBuild installs the ukhsa_github package which is used to create, alter, and audit GitHub repositories
- All repo_config.yml files within ./config_files are parsed and used to configure new repositories
- Logs from this build process are sent to S3 via CloudWatch.
- Users receive a notification via SNS/Chatbot that their repository was un/successfully created.
