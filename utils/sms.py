import os
import json
from twilio.rest import Client
#  Make sure that you type “source secrets.sh “
#  into the command line or source whatever file you kept all your tokens, etc. in


ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN =  os.environ.get('TWILIO_AUTH_TOKEN')
NOTIFY_SERVICE_SID = os.environ.get('TWILIO_NOTIFY_SERVICE_SID')
SENDER_PHONE =  os.environ.get('TWILIO_SENDER_PHONE')
TEST_RECEIVER_PHONE =  os.environ.get('TWILIO_TEST_RECEIVER_PHONE')

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_sample_sms():
    message = client.messages \
                .create(
                     body="Hello, your pet's appointment is in 1 hour.",
                     from_=SENDER_PHONE,
                     to=TEST_RECEIVER_PHONE
                 )

    print(message.sid)

def send_sample_sms_with_body(body_text):
    message = client.messages \
                .create(
                     body=body_text,
                     from_=SENDER_PHONE,
                     to=TEST_RECEIVER_PHONE
                 )

    print(message.sid)