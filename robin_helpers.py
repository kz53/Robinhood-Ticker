# data structures
price_arr = []
time_price = [(0,165.0)]
    #(time, objects, volume)

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
    return True
    
def print_account_holdings():
    return True
    
def print_account_total_value():
    return True
    
def print_account_balance():
    return True
    
def kill_all_process():
    return True    

def print_order_buy_response():
    return True
    
def print_order_sell_value():
    return True
    
def print_portfolio():
    for s in portfolio:
        print(s)

def output_to_log_file():
    return True

def SMA(time_frame, start_time=None):
    if start_time is None: 
        data_points = price_tuple_arr[(start_time-1*time_frame):start_time] 
    else: 
        data_points = price_tuple_arr[:(-1*time_frame)]
    return sum(data_points)/time_frame

def slo(start, time_interval): 
    t2 = start
    t1 = start - time_interval
    return (time_price[t2][1]-time_price[t1][1])/time_interval

def linreg(time_frame, start_time=None):
    get_valid_pts()


    return slope