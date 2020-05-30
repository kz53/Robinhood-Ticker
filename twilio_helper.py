
from twilio.rest import Client
import time
from config import twilio_usr_name, twilio_password

account_sid = twilio_usr_name
auth_token = twilio_password

client = Client(account_sid, auth_token)

def send_msg(msg_str):
    message = client.messages \
               .create(
                    body=msg_str,
                    from_='+12015716393',
                    to='+12674756252'
                )

    print(message.sid)

def notify_error_msg():
    message = client.messages.create(body='ALERT: ticker.py has failed.',from_='+12015716393',to='+12674756252')
