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
