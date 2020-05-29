import robin_stocks as robin
# import robin_helpers as helper 
import pprint
from time import sleep
from datetime import datetime
import pytz 
# import config 
import twilio_helper as twilio
import numpy as np
from talib import LINEARREG_SLOPE

#----------------------------
# helpers
def time_stamp():   
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_now.strftime("%b-%d, %Y: %H:%M:%S")
    print(dt_string)
    return dt_string

def buy(quantity):
    price = 147.87
    twilio.send_msg("Bought " + str(quantity) + "shares @ $" + str(price))
#----------------------------
# MODELS:
TA_List = np.full(23500,-1)
portfolio = robin.get_current_positions()
ms_stocks = portfolio['MSFT']['quantity']
# Linear_reg_list = []
#----------------------------
# CONFIG 
funds = 0
permitted = False
stock_symbol = "MSFT"

#-------

# log in
robin.login(config.rh_usr_name, config.rh_password)

# get current holdings
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

# initialize
principal = 10000
curr_price = float(robin.get_latest_price(test_symbol)[0])
prev_price = float(robin.get_latest_price(test_symbol)[0])
time_interval = 300
f = open("raw-output1/raw-output-{month_str}-{day_str}-{year_str}.txt", "a")
i = 0
entry_price  = float(robin.get_latest_price(test_symbol)[0])
sleep(500)
curr_price = float(robin.get_latest_price(test_symbol)[0])

# filling
for (i = 0, i<15, i++): 
    price = robin.get_latest_price(stock_symbol)[0]
    TA_List[i] = float(price)
    f.write(price)
    sleep(1)
 
#--------

# MAIN LOOP
while(permitted && i<23500 ):
    try:
        price = robin.get_latest_price("MSFT")[0]

        #f.write(time_stamp())
        f.write(price+"\n")
        #f.write("--------------------------------\n")
        f.flush()
        
        TA_List[i] = float(price) 

        perform_ta(i, 15)

        if stocks == 0 && ^^^ :
          BUY()
        elif stocks > 0  && ^^^ :
          HOLD()
        elif stocks == 0 && VVV :
          HOLD()
        elif stocks > 0 stocks && VVV:
          SELL()
    except:
        #f.write("-1"+"\n")
        #f.flush()
        if failed:
            twilio.notify_error_msg()
            failed = True
    i += 1

def perform_ta(arr):
    for i in arr: 
        if i != -1:
    np.build
    slope = LINEARREG_SLOPE()
    return slope


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

def BUY():
    fdsf

def SELL():
    es;krer

def HOLD():
    sdfls;k 

robin.logout()


def perform_ta(i, period=15):
    if (i-period < 0):
        start = 0
    else:
        start = i + 1 - period

    end = i + 1
    data = TA_LIST[start:end] 
    cleaned_data = []
    for x in data:
        if x != -1:
            cleaned_data.append(x)
        else:
            cleaned.data.append(nan)

    slope = LINEARREG_SLOPE(np.array(cleaned_data), period)
    return slope


    
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

