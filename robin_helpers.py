# Returns string in form of "Month Day, Year: hh:mm:ss "
def time_stamp():
    utc_now = pytz.utc.localize(datetime.utcnow())
    est_now = utc_now.astimezone(pytz.timezone("America/New_York")) 
    dt_string = est_0now.strftime("%b-%d, %Y: %H:%M:%S")
    print(dt_string)
    return dt_string

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