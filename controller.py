from time import sleep
from datetime import datetime
import robin_stocks as robin
import pytz
import config 
import pprint
# import twilio_helper as twilio

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

robin.login(config.rh_usr_name, config.rh_password)
portfolio = robin.build_holdings() 
print(portfolio['SNAP']['quantity'])

def confirm(symb):
    resp = robin.build_holdings()[symb]['quantity']
    if resp == portfolio[symb]['quantity']:
        print(resp)
        return True
    else:
        print('Falsehoods!')
        return False

def buy(symb,qty,price):
	confirm(symb)
    # resp = robin.order_buy_limit(symb, qty, price)
    # if resp["state"] == "confirmed":
        # portfolio[symb]
	confirm(symb)
    
def sell(symb,qty,price):
    confirm(symb)
    resp = robin.order_sell_limit(symb, qty, price)
    # if resp["state"] == "confirmed":
    #     portfolio[symb]
    confirm(symb) 

def cancel():
    print(robin.get_all_open_stock_orders())

print(robin.get_all_open_stock_orders())

# {'id': 'c65b6b57-f39f-4c0e-ac9d-1ead624dd560', 'ref_id': '19615503-0c80-40d3-8e60-a004bbbe3315', 'url': 'https://api.robinhood.com/orders/c65b6b57-f39f-4c0e-ac9d-1ead624dd560/', 'account': 'https://api.robinhood.com/accounts/691500961/', 'position': 'https://api.robinhood.com/positions/691500961/1e513292-5926-4dc4-8c3d-4af6b5836704/', 'cancel': 'https://api.robinhood.com/orders/c65b6b57-f39f-4c0e-ac9d-1ead624dd560/cancel/', 'instrument': 'https://api.robinhood.com/instruments/1e513292-5926-4dc4-8c3d-4af6b5836704/', 'cumulative_quantity': '0.00000000', 'average_price': None, 'fees': '0.00', 'state': 'unconfirmed', 'type': 'limit', 'side': 'buy', 'time_in_force': 'gtc', 'trigger': 'immediate', 'price': '20.00000000', 'stop_price': None, 'quantity': '1.00000000', 'reject_reason': None, 'created_at': '2020-06-17T02:33:09.023330Z', 'updated_at': '2020-06-17T02:33:09.088431Z', 'last_transaction_at': '2020-06-17T02:33:09.023330Z', 'executions': [], 'extended_hours': False, 'override_dtbp_checks': False, 'override_day_trade_checks': False, 'response_category': None, 'stop_triggered_at': None, 'last_trail_price': None, 'last_trail_price_updated_at': None, 'total_notional': {'amount': '20.00', 'currency_code': 'USD', 'currency_id': '1072fc76-1862-41ab-82c2-485837590762'}, 'executed_notional': None, 'investment_schedule_id': None}
