<<<<<<< HEAD
import requests
import hashlib
import hmac
import time
from config import api_key, api_secret, base_url

# Common functions
def get_server_time():
    # Retrieve server time from the API.
    response = requests.get(base_url + '/fapi/v1/time')
    server_time = response.json()['serverTime']
    print(f"Server time: {server_time}")
    return server_time

def create_signature(query_string, secret):
    # Create HMAC SHA256 signature for the query string using the secret key.
    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    print(f"Signature: {signature}")
    return signature

def get_positions(api_key, api_secret):
    # Retrieve positions from the API.
    endpoint = '/fapi/v2/positionRisk'
    timestamp = get_server_time()

    query_string = f'timestamp={timestamp}'
    signature = create_signature(query_string, api_secret)
    
    headers = {
        'X-MBX-APIKEY': api_key
    }
    
    response = requests.get(base_url + endpoint + '?' + query_string + '&signature=' + signature, headers=headers)
    positions = response.json()
    return positions

def has_positions(api_key, api_secret, symbol):
    # Check if there are any positions for the given symbol.
    print("Checking positions...")
    positions = get_positions(api_key, api_secret)
    has_long = False
    has_short = False

    for position in positions:
        if position['symbol'] == symbol:
            if position['positionSide'] == 'LONG' and float(position['positionAmt']) > 0:
                has_long = True
            elif position['positionSide'] == 'SHORT' and float(position['positionAmt']) < 0:
                has_short = True

    print(f"Has LONG: {has_long}, Has SHORT: {has_short}")
    return has_long, has_short

def check_if_positions_exist(symbol):
    # Check if there are any long or short positions for the given symbol.
    has_long, has_short = has_positions(api_key, api_secret, symbol)
    return has_long, has_short

def change_leverage(symbol, leverage, api_key, api_secret):
    # Change the leverage for a specific symbol.
    print("Changing leverage...")
    endpoint = '/fapi/v1/leverage'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'leverage': leverage,
        'timestamp': timestamp
    }
    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    signature = create_signature(query_string, api_secret)
    params['signature'] = signature
    
    headers = {
        'X-MBX-APIKEY': api_key
    }

    response = requests.post(base_url + endpoint, headers=headers, data=params)
    print(f"Leverage change response: {response.json()}")
    return response.json()

def change_margin_type(symbol, margin_type, api_key, api_secret):
    # Change the margin type for a specific symbol.
    print("Changing margin type...")
    endpoint = '/fapi/v1/marginType'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'marginType': margin_type,
        'timestamp': timestamp
    }
    
    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    signature = create_signature(query_string, api_secret)
    params['signature'] = signature
    
    headers = {
        'X-MBX-APIKEY': api_key
    }

    response = requests.post(base_url + endpoint, headers=headers, data=params)
    print(f"Margin type change response: {response.json()}")
    return response.json()

def get_market_price(symbol, api_key, api_secret):
    # Retrieve the current market price for a specific symbol.
    try:
        endpoint = '/fapi/v1/ticker/price'
        params = {
            'symbol': symbol
        }

        response = requests.get(base_url + endpoint, params=params)
        print("Market price response:", response.text)

        if response.status_code == 200:
            return float(response.json()['price'])
        else:
            print("Error: Failed to get market price. Status code:", response.status_code)
            return None
    except Exception as e:
        print(f"Error getting market price: {e}")
        return None
    
def get_open_orders(symbol, api_key, api_secret):
    # Retrieve the list of open orders for a specific symbol.
    try:
        endpoint = '/fapi/v1/openOrders'
        timestamp = int(time.time() * 1000)
        params = {
            'symbol': symbol,
            'timestamp': timestamp
        }

        query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
        signature = create_signature(query_string, api_secret)
        params['signature'] = signature

        headers = {
            'X-MBX-APIKEY': api_key
        }

        print("Getting open orders...")
        print("Params:", params)
        print("Query string:", query_string)

        response = requests.get(base_url + endpoint, headers=headers, params=params)
        print("Open orders response:", response.text)

        if response.status_code == 200:
            return response.json()
        else:
            print("Error: Failed to get open orders. Status code:", response.status_code)
            print(response.json())
            return None
    except Exception as e:
        print(f"Error getting open orders: {e}")
        return None
=======
import requests
import hashlib
import hmac
import time
from config import api_key, api_secret, base_url

def get_server_time():
    response = requests.get(base_url + '/fapi/v1/time')
    server_time = response.json()['serverTime']
    print(f"Server time: {server_time}")
    return server_time

def create_signature(query_string, secret):
    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    print(f"Signature: {signature}")
    return signature

def get_positions(api_key, api_secret):
    endpoint = '/fapi/v2/positionRisk'
    timestamp = get_server_time()

    query_string = f'timestamp={timestamp}'
    signature = create_signature(query_string, api_secret)
    
    headers = {
        'X-MBX-APIKEY': api_key
    }
    
    response = requests.get(base_url + endpoint + '?' + query_string + '&signature=' + signature, headers=headers)
    positions = response.json()
    #print(f"Positions: {positions}")
    return positions

def has_positions(api_key, api_secret, symbol):
    print("Checking positions...")
    positions = get_positions(api_key, api_secret)
    has_long = False
    has_short = False

    for position in positions:
        if position['symbol'] == symbol:
            if position['positionSide'] == 'LONG' and float(position['positionAmt']) > 0:
                has_long = True
            elif position['positionSide'] == 'SHORT' and float(position['positionAmt']) < 0:
                has_short = True

    print(f"Has LONG: {has_long}, Has SHORT: {has_short}")
    return has_long, has_short

def check_if_positions_exist(symbol):
    has_long, has_short = has_positions(api_key, api_secret, symbol)
    return has_long, has_short
>>>>>>> c583115c0c7a00e55126e5566ba9834a94730215
