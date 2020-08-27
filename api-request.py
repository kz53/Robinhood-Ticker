from time import sleep
from datetime import datetime
import robin_stocks as robin
import pytz
import config 
import pprint
import twilio_helper as twilio

robin.login(config.rh_usr_name, config.rh_password)

#API call goes here
#---------------------------------
resp = robin.get_latest_price('SHOP')
#---------------------------------
print(resp)

robin.logout()