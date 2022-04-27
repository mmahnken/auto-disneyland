from twilio.rest import Client
import os

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

def send_message(content, recipients):
     client = Client(account_sid, auth_token)
     for r in recipients:
          message = client.messages \
                          .create(
                               body=content,
                               from_='+14422504031',
                               to=r,
                           )
          print(f"SENT MESSAGE {message.sid} SUCCESSFULLY")