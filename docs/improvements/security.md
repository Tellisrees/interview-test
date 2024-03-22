# Security
- Placing a pull request in between repo request and provisioning slows down development, compared to the original implementation which allowed users to create requests freely.  However, the security benefit of my solution is that it adds two layers of config validation (automatic and human) before repos are created.
- Placing secrets like GH tokens in AWS Secrets Manager is a best practice.
- The original implementation does not deposit any logs to AWS for future perusal.  As such, it would be difficult to diagnose potential issues.  Using CodeBuild provides easy integration with CloudWatch which can deposit logs to a dedicated S3 bucket.
- Although it is possible to interact with AWS from a GitHub actions runner via Boto, this requires storing AWS credentials as GitHub secrets, which increases the attack surface.  As such it is more secure to use CodeBuild which does not require that any secrets are stored in GitHub. 
- Expanded gitignore in the main repo.



## If I had more time
- I would have set up an automated script with EventBridge-Lambda-SES to alert administrators when the GH token was close to expiration
- If the package was going to be shared more widely, would want to consider the licence used
- If other areas of the codebase were considered sensitive, could migrate to S3 (encrypt at rest) and have CodeBuild pull in as and when needed.
- It doesn't seem possible to make creating a repo and e.g. adding a gitignore file a single atomic action, meaning there is a possibility for repos to be created without adequate security measures in place.  I would implement a second class (RepoAuditor) to check that repos were following best practices at the end of the creation process, and only then send success messages to users.  The RepoAuditor could also be run on a schedule to collect information on all of the organisation's repos and collate findings in a single report.

# To Do
- 