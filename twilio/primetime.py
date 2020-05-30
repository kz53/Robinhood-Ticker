from twilio.rest import Client
import time 

account_sid = 'AC239248855693095338a44f03f7a37803'
auth_token = 'a867e61f710d60e5e0e2f6e7bd8097f7'
client = Client(account_sid, auth_token)

x = 0
while(x<3):
    time.sleep(5)
    print("tik")
    message = client.messages \
                .create(
                     body="Poke.",
                     from_='+12015716393',
                     to='+12674756252' 
                )

    print(message.sid)
    x += 1
