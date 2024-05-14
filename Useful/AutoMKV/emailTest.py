import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def send_email_aws_ses(message, subject, recipient):
    # Create a new SES resource and specify a region.
    ses_client = boto3.client('ses', region_name='us-west-2')  # Replace with your region

    try:
        # Provide the contents of the email.
        response = ses_client.send_email(
            Source='MKV.Notifications@passpals.net',  # Replace with your verified email
            Destination={
                'ToAddresses': [recipient],
            },
            Message={
                'Subject': {
                    'Data': subject,
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': message,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )
        print("Email sent! Message ID:"),
        print(response['MessageId'])

    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials")
    except Exception as e:
        print("Error sending email: ", e)

# Example usage:
send_email_aws_ses("The disk is done!", "", "7206447060@vtext.com")
