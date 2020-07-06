from time import sleep
from datetime import datetime
import pytz
import pprint
import twilio_helper as twilio

utc_now = pytz.utc.localize(datetime.utcnow())

failed = False

day = utc_now.strftime("%d")
month = utc_now.strftime("%m")
year = utc_now.strftime("%y")
date = year + month + day

def time_stamp():
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_now.strftime("%b-%d, %Y: %H:%M:%S") + "\n"
    print(dt_string)
    return dt_string


# get request to stock twits 
# filter out all the ones with ticker symbols 
# open lionmessages.txt
# load previous x msg
# compare which ones are repeats
# send twilio message for ones that aren't 
# write ones that aren't




print("finished")
