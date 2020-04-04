# Returns string in form of "Month Day, Year: hh:mm:ss "
def time_stamp():
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_now.strftime("%b-%d, %Y: %H:%M:%S")
    print(dt_string)
    return dt_string

class sma:
    values = []
    sma_period = 1    
    
    def __init__(self, time_period):
        sma_period = time_period
    
    def add_value(val):
        values.append(val)
        if len(values) > sma_period:
            values.pop()    
            return sum(values)/sma_period
        else:
            return -1

# Returns float to 2 decimal places
def get_price(symbol):
    round(float(robin.get_latest_price(symbol)[0]), 2)

def round_to_2(x , places=2):
    return round(x, places)

def print_account_balance():

def print_account_holdings():

def print_account_total_value():

def print_account_balance():

def kill_all_process():


def print_order_buy_response():

def print_order_sell_value():

def print_portfolio():
    for s in portfolio:
        print(s)


def output_to_log_file():
