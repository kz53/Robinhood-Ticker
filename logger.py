from time import sleep
from datetime import datetime

def time_stamp():
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_now.strftime("%b-%d, %Y: %H:%M:%S")
    print(dt_string)
    return dt_string

f = open("test-log-file.txt", "a")
f.write("Time Log: \n")
while(true):
    f.write(time_stamp())
    f.flush()
    sleep(2)
f.close()