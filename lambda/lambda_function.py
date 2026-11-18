import boto3
import csv
import io
import os


# Initialize AWS clients
s3_client = boto3.client('s3')
ses_client = boto3.client('ses')


def lambda_handler(event, context):


    # S3 bucket name
    bucket_name = 'serverless-email-marketing-miniproject'


    try:
        # 1. Retrieve contacts.csv from S3
        csv_file = s3_client.get_object(
            Bucket=bucket_name,
            Key='contacts.csv'
        )


        csv_content = csv_file['Body'].read().decode('utf-8-sig')


        # Skip blank lines before the headers
        nonblank_lines = [
            line for line in csv_content.splitlines()
            if line.strip()
        ]


        if not nonblank_lines:
            raise ValueError("contacts.csv is empty.")


        # Parse CSV using the first nonblank line as headers
        reader = csv.DictReader(io.StringIO('\n'.join(nonblank_lines)))


        # Clean column headers
        if reader.fieldnames:
            reader.fieldnames = [
                name.strip() for name in reader.fieldnames
            ]


        # Validate required columns
        required_columns = {'FirstName', 'Email'}


        if not reader.fieldnames or not required_columns.issubset(
            set(reader.fieldnames)
        ):
            raise ValueError(
                "CSV must contain FirstName and Email headers."
            )


        # 2. Retrieve email template from S3
        email_template = s3_client.get_object(
            Bucket=bucket_name,
            Key='email_template.html'
        )


        email_html = email_template['Body'].read().decode('utf-8')


        # 3. Process contacts and send personalized emails
        sent_count = 0


        for contact in reader:


            # Skip completely empty rows
            if not contact or not any(
                value and value.strip()
                for value in contact.values()
                if isinstance(value, str)
            ):
                continue


            # Clean values and handle missing fields
            first_name = (contact.get('FirstName') or '').strip()
            recipient_email = (contact.get('Email') or '').strip()


            if not first_name or not recipient_email:
                print(f"Skipping incomplete contact: {contact}")
                continue


            # Personalize the HTML template
            personalized_email = email_html.replace(
                '{{FirstName}}',
                first_name
            )


            # Send email using Amazon SES
            response = ses_client.send_email(
             Source=os.environ['SENDER_EMAIL'],
                Destination={
                    'ToAddresses': [recipient_email]
                },
                Message={
                    'Subject': {
                        'Data': 'Your Weekly Codify Mail!',
                        'Charset': 'UTF-8'
                    },
                    'Body': {
                        'Html': {
                            'Data': personalized_email,
                            'Charset': 'UTF-8'
                        }
                    }
                }
            )


            sent_count += 1


            print(
                f"Email sent to {recipient_email}: "
                f"MessageId {response['MessageId']}"
            )


        return {
            'statusCode': 200,
            'body': f'Email processing completed. Emails sent: {sent_count}'
        }


    except Exception as e:
        print(f"An error occurred: {e}")
        raise
