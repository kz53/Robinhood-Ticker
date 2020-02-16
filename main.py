# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import robin_stocks from '' as robin

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)

# Robin Stocks begin
robin.login(<username>,<password>)

# stock
robin.get_fundamentals()
robin.get_historicals('SHOP', span='day', bounds='regular')

# account
robin.get_current_positions()

robin.build_holdings()
robin.build_user_profile()

# order
robin.cancel_all_open_orders()
robin.cancel_order
robin.get_order_info()
robin.order_buy_market('SHOP',1)
robin.order_sell_market()
robin.order_buy_limit()
robin.order_sell_limit('SHOP',1,520)

order_buy_stop_limit()
order_buy_stop_loss()
order_sell_stop_limit()
order_sell_stop_loss()
robin.logout()