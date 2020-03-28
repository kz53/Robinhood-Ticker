import robin_stocks as robin
# import robin_helpers as helper 
import pprint
from time import sleep
from datetime import datetime
import pytz 
# import config 
import twilio_helper as twilio
#----------------------------
# helpers
def time_stamp():   
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_0now.strftime("%b-%d, %Y: %H:%M:%S")
    print(dt_string)
    return dt_string

def buy(quantity):
    price = 147.87
    twilio.send_msg("Bought " + str(quantity) + "shares @ $" + str(price))
#----------------------------

print(config.secret)
# log in
robin.login(config.rh_usr_name, config.rh_password)

# get current holdings
portfolio = robin.get_current_positions()
    # {
    # 'I':{
    #         'price': '4', 
    #         'quantity': '3070', 
    #         'average_buy_price': '5', 
    #         'equity': '13792.28', 
    #         'percent_change': '-10.58', 
    #         'equity_change': '-1631.705000', 
    #         'type': 'stock', 
    #         'name': 'Intelsat', 
    #         'id': 'b12f8af0-5c02-4ac3-b91b-c6557a78c19e', 
    #         'pe_ratio': None, 
    #         'percentage': '52.22'
    #     },
    # 'SPY':{},
    # 'SHOP':{}
    # }

test_symbol= 'SHOP'
principal = 10000
curr_price = float(robin.get_latest_price(test_symbol)[0])
prev_price = float(robin.get_latest_price(test_symbol)[0])
permitted = False
time_interval = 300
# ticker information
while(permitted):
    seconds = 0
    entry_price = float(robin.get_latest_price(test_symbol)[0])
    sleep(500)
    curr_price = float(robin.get_latest_price(test_symbol)[0])

    while (seconds < time_interval):
        curr_price = floatx(robin.get_latest_price(test_symbol)[0])
        if (curr_price > entry_price):
            if (portfolio[test_symbol] != None): 
                buy(test_symbol)
        else:
            if (portfolio[test_symbol] != None): 
                sell(test_symbol)
        wait(1)
        output_to_log_file()
        seconds += 1
# {"SHOP":{price:500, price_bought:525, shares_quant:}}
#
# SHOP [500, 501,502, 505, 505, 510, 499, 501]
#

buy(7)


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

