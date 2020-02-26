import robin_stocks from '' as robin
import pprint
from time import sleep
from datetime import datetime
import pytz 

#----------------------------
# helpers
def time_stamp():
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_0now.strftime("%b-%d, %Y: %H:%M:%S")
    print(dt_string)
    return dt_string
#----------------------------
amt_shop = 0

# log inz
robin.login(<username>,<password>)

# get current holdings
robin.get_current_positions()
prev_price = float(robin.get_latest_price('SHOP')[0])
# get shop price

# ticker information
while(true):
    sleep(500)
    curr_price = float(robin.get_latest_price('SHOP')[0])
    print(curr_price)

    curr_price = float(robin.get_latest_price('SHOP')[0])
    if curr_price >= prev_price:
        if amt_shop == 0: 
            robin.order_buy_limit('SHOP', 1, curr_price)
            amt_shop = 1
        else: 
            # wait
    else:
        if amt_shop > 0: 
            robin.sell_order_limit('SHOP', 1, curr_price )   
            amt_shop = 0
    prev_price = curr_price

portfolio = {}
# {"SHOP":{price:500, price_bought:525, shares_quant:}}
#
# SHOP [500, 501,502, 505, 505, 510, 499, 501]
#


robin.logout()

#-------------------------------------
#get matplotlib
#watchlist of symbols 
#{SYMB:price, shares, buy_price, sell_price, slope}
#slope
#acceleration
#volume
#total_volume
#channel 
#
# # execute buy order
# if curr_price < 550:
#     robin.order_buy_limit('SHOP', 1, 525.25)

# # get current holdings
# robin.get_current_positions()z

