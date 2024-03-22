# CI/CD
- I use a combination of GitHub actions and AWS Codebuild to automate the task
- Users create YAML config files for the repos that they want to create, these are validated by GitHub actions-triggered pytest when pull-request is created 
- When engineers approve the pull-request, a CodeBuild hook causes the package to create a new repo for each config file that it processes

## If I had more time
- I would have set up Tox so that tests could be run on multiple python versions
- I would have set up a pre-commit hook to run black on source code

# To Do
- On pull request - tests for Black
- On pull request - tests package
- On pull request - tests config files
- Update the buildspec file

