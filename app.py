import robin_stocks from '' as robin
from time import sleep

amt_shop = 0

# log in
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


# # execute buy order
# if curr_price < 550:
#     robin.order_buy_limit('SHOP', 1, 525.25)

# # get current holdings
# robin.get_current_positions()


robin.logout()

