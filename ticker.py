from time import sleep
from datetime import datetime
import robin_stocks as robin
import pytz
import config 
import pprint

robin.login(config.rh_usr_name, config.rh_password)

def time_stamp():
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_now.strftime("%b-%d, %Y: %H:%M:%S") + "\n"
    print(dt_string)
    return dt_string

f = open("raw-output-3-9-20.txt", "a")
i = 0
while(i<24000):
    #f.write(time_stamp())
    price = robin.get_latest_price("MSFT")[0]
    f.write(price+"\n")
    #f.write("--------------------------------\n")
    f.flush()
    i += 1
    sleep(1)
f.close()
robin.logout()
print("finished")
