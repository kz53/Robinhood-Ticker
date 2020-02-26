from time import sleep
from datetime import datetime

def time_stamp():
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_0now.strftime("%b-%d, %Y: %H:%M:%S")
    print(dt_string)
    return dt_string

f = open("test-log-file.txt", "a")
f.write(time_stamp())
while(true):
    f.write(time_stamp())
    sleep(5)
f.close()