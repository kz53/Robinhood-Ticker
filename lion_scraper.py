# COPY ME DONT EDIT

import requests
import json
import csv
from time import sleep
from datetime import datetime
import pytz
import pprint
import twilio_helper as twilio

filename = 'lion-posts.csv'
messages_id = set()
f = open(filename, 'r', newline='', encoding='utf-8')
csv_reader = csv.reader(f)
for row in csv_reader:
    try:
        if row[0] != 'id':
            messages_id.add(float(row[0]))
    except:
        twilio.send_msg("lion_scraper has failed")

print(messages_id)
f.close()

def sanitize_str(s):
    result = s.replace('\n', ' ')
    return result

f = open(filename, 'a', newline='', encoding='utf-8')
csv_writer = csv.writer(f, delimiter=',',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
#GET
#-------------------
res = requests.get('https://api.stocktwits.com/api/2/streams/user/lionmaster.json')
#-------------------

# IF JSON
res_dict = res.json()
print("num messages: "+str(len(res_dict['messages'])))
res_dict['messages'].reverse()
for msg in res_dict['messages']:
    if 'symbols' in msg:
        if msg['id'] not in messages_id:
            try:
                symbs = ""
                for x in msg['symbols']:
                    if symbs == "":
                        symbs += x['symbol']
                    else:
                        symbs += ','+x['symbol']
                row = []
                row.append(msg['id'])
                row.append(sanitize_str(msg['body']))
                row.append(msg['created_at'])
                row.append(symbs)
                # print(msg['id'])
                # print(msg['body'])
                # print(msg['created_at'])
                csv_writer.writerow(row)
                twilio.send_msg(msg['body'])
            except:
                twilio.send_msg("lion_scraper has failed")


f.close()


utc_now = pytz.utc.localize(datetime.utcnow())
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






print("finished")
