from time import sleep
from datetime import datetime
import pytz
import sys

def time_stamp():
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_now.strftime("%b-%d: %H:%M:%S \n")
    print(dt_string)
    return dt_string

f = open("test-log-file.txt", "a")
f.write("Time log:\n")
while(True):
    #print("hello world")
    f.write(time_stamp())
    f.flush()
    sleep(2)
f.close()
