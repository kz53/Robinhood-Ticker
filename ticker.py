from time import sleep
from datetime import datetime
import robin_stocks as robin
import pytz
import config 
import pprint
import twilio_helper as twilio
robin.login(config.rh_usr_name, config.rh_password)

utc_now = pytz.utc.localize(datetime.utcnow())

failed = False
day_str = utc_now.strftime("%d")
month_str = utc_now.strftime("%m")
year_str = utc_now.strftime("%y")

def time_stamp():
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_now.strftime("%b-%d, %Y: %H:%M:%S") + "\n"
    print(dt_string)
    return dt_string

f = open(f"../raw-output-files/{month_str}-{day_str}-{year_str}-raw-output.txt", "a")
i = 0
while(i<23500):
    try:
        #f.write(time_stamp())
        price = robin.get_latest_price("MSFT")[0]
        f.write(price+"\n")
        #f.write("--------------------------------\n")
        f.flush()
    except:
        f.write("-1"+"\n")
        f.flush()
        if failed:
            twilio.notify_error_msg()
            failed = True
    i += 1
    sleep(1)
f.close()
robin.logout()
print("finished")
