from twilio.rest import Client
import time 

account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)


while(true):
    time.sleep(5000)
    print("tik")
    message = client.messages \
                .create(
                     body="Poke.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

    print(message.sid)