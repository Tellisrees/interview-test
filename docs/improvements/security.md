# Security
- Placing a pull request in between repo request and provisioning slows down development, compared to the original implementation which allowed users to create requests freely.  However, the security benefit of my solution is that it adds two layers of config validation (automatic and human) before repos are created
- Placing secrets like GH tokens in AWS Secrets Manager is a best practice


## If I had more time
- I would have set up an automated script with EventBridge-Lambda-SES to alert administrators when the GH token was close to expiration

# To Do
- 