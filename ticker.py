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

day = utc_now.strftime("%d")
month = utc_now.strftime("%m")
year = utc_now.strftime("%Y")
date = year+'-'+month+'-'+day

watchlist_symbols=[
    'MSFT',
    'SHOP',
    'GOOG',
    'SNAP',
    'TSLA',
    'BA',
    'BYND',
    'SPCE',
    'UBER',
    'COST',
    'DIS',
]

filenames = []
for symb in watchlist_symbols:
    name = f'../secdata/{symb}/{symb}-{date}-secdata.txt'
    filenames.append(name)

files = [open(f, "a") for f in filenames] 

def time_stamp():
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_now.strftime("%b-%d, %Y: %H:%M:%S") + "\n"
    print(dt_string)
    return dt_string


twilio.send_key_msg('start')

i = 0
while(i<23300):
    try:
        #f.write(time_stamp())
        resp = robin.get_latest_price(watchlist_symbols)
        for j in range(len(files)):
            f = files[j]
            f.write(resp[j]+'\n')
            f.flush()
            #f.write("--------------------------------\n")
    except:
        for j in range(len(files)):
            f = files[j]
            f.write('-1'+',\n')
            f.flush()
        if not failed:
            twilio.notify_error_msg()
            failed = True
    i += 1
    sleep(1)

f.close()
robin.logout()
twilio.send_key_msg('end')
print("finished")
