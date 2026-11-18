# Serverless Email Marketing System Using AWS

## 1. Project Overview

The Serverless Email Marketing System is a cloud-based mini-project developed using Amazon Web Services (AWS). It automates the process of sending personalized email newsletters to multiple recipients.

The system uses AWS Lambda to execute the email-processing logic, Amazon S3 to store contact information and HTML email templates, Amazon SES to send emails, and Amazon EventBridge to support scheduled execution.

## 2. Objectives

- To develop an automated email marketing system using AWS serverless services.
- To store contact information and email templates in Amazon S3.
- To generate personalized emails using AWS Lambda and Python.
- To send emails using Amazon Simple Email Service (SES).
- To support scheduled execution using Amazon EventBridge.

## 3. AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon S3 | Stores contacts.csv and email_template.html |
| AWS Lambda | Processes contacts and generates personalized emails |
| Amazon SES | Sends emails to recipients |
| Amazon EventBridge | Supports scheduled triggering of Lambda |
| AWS IAM | Manages permissions for accessing AWS services |

## 4. Technologies Used

- Python
- Boto3
- Amazon Web Services
- HTML
- CSV

## 5. Project Workflow

1. Contact information and the HTML email template are stored in an Amazon S3 bucket.
2. Amazon EventBridge can trigger the Lambda function according to a configured schedule.
3. AWS Lambda retrieves the CSV file and HTML template from S3.
4. Lambda processes the contact information and personalizes the email using the recipient's name.
5. Amazon SES sends the personalized emails to the recipients.
6. Execution details and email message IDs are recorded in CloudWatch logs.

## 6. Project Execution Result

The Lambda function was successfully tested. The execution output reported that email processing was completed and three email send requests were successfully processed by Amazon SES.

## 7. Repository Structure

```text
serverless-email-marketing-aws/
├── lambda/
│   └── lambda_function.py
├── iam/
│   └── iam_policy.json
├── templates/
│   └── email_template.html
├── events/
│   └── test_event.json
├──Implementation_Screenshots/
├── .gitignore
└── README.md
```

## 8. Implementation Screenshots

Screenshots of the AWS implementation, including S3, Lambda, IAM, EventBridge, SES, and execution output, are available in the `Implementation_Screenshots` folder.

## 9. Security and Configuration Notes

- The contacts CSV file is not included in this public repository to protect recipient information.
- The sender email address is configured using the Lambda environment variable `SENDER_EMAIL`.
- AWS IAM permissions are used to control access to S3 and SES.
- AWS credentials and secret keys should never be uploaded to GitHub.

## 10. Conclusion

This project demonstrates how AWS serverless services can be integrated to build an automated email marketing system. It provides practical experience with cloud storage, serverless computing, event scheduling, access management, and email delivery.

