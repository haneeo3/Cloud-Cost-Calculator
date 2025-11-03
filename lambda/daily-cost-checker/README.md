## Deployment

1. Create an IAM role with:
   - AWSLambdaBasicExecutionRole
   - ce:GetCostAndUsage
   - sns:Publish
2. Create the Lambda function `daily-cost-checker` using this code.
3. Create an SNS topic and subscribe your email.
4. Add an EventBridge rule to trigger the Lambda daily.
