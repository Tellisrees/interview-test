# CI/CD
- I use a combination of GitHub actions and AWS Codebuild to automate the task
- Users create YAML config files for the repos that they want to create, these are validated by GitHub actions-triggered pytest when pull-request is created 
- When engineers approve the pull-request, a CodeBuild hook causes the package to create a new repo for each config file that it processes

## If I had more time
- I would have set up Tox so that tests could be run on multiple python versions
- I would have set up a pre-commit hook to run black on source code
- I would have developed an alerting method in the RepoConfigurer class that would automatically send a message to relevant users via SES/SNS/Chatbot when a repo was un/successfully created/modified.  This makes debugging easier (users don't have to search in S3 logs) and all members of teams related to particular repos are notified (i.e. not just the person that submitted the config file) 
- As it stands, the code does not check if a repo defined in a user file has already been created, and so returns errors.  I would extend the logic to check if a repo has already been created.  If it has, update it according to the config file, rather than create it.  This would involve a bit of refactoring in the RepoConfigurer class.


