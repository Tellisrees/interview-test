# Security
- Placing a pull request in between repo request and provisioning slows down development, compared to the original implementation which allowed users to create requests freely.  However, the security benefit of my solution is that it adds two layers of config validation (automatic and human) before repos are created.
- Placing secrets like GH tokens in AWS Secrets Manager is a best practice.
- The original implementation does not deposit any logs to AWS for future perusal.  As such, it would be difficult to diagnose potential issues.  Using CodeBuild provides easy integration with CloudWatch which can deposit logs to a dedicated S3 bucket.
- Although it is possible to interact with AWS from a GitHub actions runner via Boto, this requires storing AWS credentials as GitHub secrets, which increases the attack surface.  As such it is more secure to use CodeBuild which does not require that any secrets are stored in GitHub 


## If I had more time
- I would have set up an automated script with EventBridge-Lambda-SES to alert administrators when the GH token was close to expiration

# To Do
- 