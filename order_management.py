import requests
import hashlib
import hmac
import time
import logging
from config import api_key, api_secret, base_url, leverage, margin_type, order_quantity, symbol, callback_rate, working_type, stop_loss_roi, take_profit_roi
from binance_futures import get_positions, get_server_time, create_signature

# Setup logger
logger = logging.getLogger('order_management')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('order_management.log')
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

def create_signature(query_string, secret):
    """Create HMAC SHA256 signature for the query string using the secret key."""
    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    print(f"Signature: {signature}")
    return signature

def change_leverage(symbol, leverage, api_key, api_secret):
    """Change the leverage for a specific symbol."""
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
    """Change the margin type for a specific symbol."""
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

def get_open_orders(symbol, api_key, api_secret):
    """Retrieve the list of open orders for a specific symbol."""
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

def open_trailing_stop_order(symbol, side, quantity, callback_rate, api_key, api_secret, position_side, working_type):
    # Cancel existing orders on the same side
    cancel_existing_orders(symbol, side, api_key, api_secret)
    
    """Open a trailing stop order."""
    print(f"Opening trailing stop order for {position_side}...")
    endpoint = '/fapi/v1/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'side': side,
        'type': 'TRAILING_STOP_MARKET',
        'quantity': round(quantity, 3),  # Round to 3 decimal places
        'callbackRate': callback_rate,
        'timestamp': timestamp,
        'positionSide': position_side,
        'workingType': working_type
    }

    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    signature = create_signature(query_string, api_secret)
    params['signature'] = signature
    
    headers = {
        'X-MBX-APIKEY': api_key
    }

    response = requests.post(base_url + endpoint, headers=headers, data=params)
    print(f"Trailing stop order response: {response.json()}")
    return response.json()

def cancel_existing_orders(symbol, side, api_key, api_secret):
    """Cancel existing open orders for a specific symbol and side."""
    open_orders = get_open_orders(symbol, api_key, api_secret)
    if open_orders is None:
        print("Failed to get open orders.")
        return
    
    for order in open_orders:
        if order['side'] == side:
            endpoint = '/fapi/v1/order'
            timestamp = int(time.time() * 1000)
            params = {
                'symbol': symbol,
                'orderId': order['orderId'],
                'timestamp': timestamp
            }

            query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
            signature = create_signature(query_string, api_secret)
            params['signature'] = signature

            headers = {
                'X-MBX-APIKEY': api_key
            }

            response = requests.delete(base_url + endpoint, headers=headers, params=params)
            if response.status_code == 200:
                print(f"Cancelled order {order['orderId']} on {symbol} side {side}")
            else:
                print(f"Failed to cancel order {order['orderId']} on {symbol} side {side}. Response: {response.text}")


def open_stop_loss_order(symbol, side, quantity, stop_price, api_key, api_secret, position_side):
    """Open a stop loss order."""
    print(f"Opening stop loss order for {position_side}...")
    endpoint = '/fapi/v1/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'side': side,
        'type': 'STOP_MARKET',
        'quantity': round(quantity, 3),  # Round to 3 decimal places
        'stopPrice': round(stop_price, 2),  # Round to 2 decimal places
        'timestamp': timestamp,
        'positionSide': position_side,
        'workingType': working_type
    }

    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    signature = create_signature(query_string, api_secret)
    params['signature'] = signature
    
    headers = {
        'X-MBX-APIKEY': api_key
    }

    response = requests.post(base_url + endpoint, headers=headers, data=params)
    print(f"Stop loss order response: {response.json()}")
    return response.json()

def get_market_price(symbol, api_key, api_secret):
    """Retrieve the current market price for a specific symbol."""
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

def check_and_set_stop_loss(symbol, position_side, api_key, api_secret):
    """Check if a stop loss order exists for a position, and create one if it doesn't."""
    positions = get_positions(api_key, api_secret)
    market_price = get_market_price(symbol, api_key, api_secret)
    
    # Calculate stop loss price based on leverage and ROI
    stop_loss_price = market_price * (1 + stop_loss_roi / leverage / 100) if position_side == 'LONG' else market_price * (1 - stop_loss_roi / leverage / 100)

    if market_price is None:
        print("Error: Could not retrieve market price.")
        return

    for position in positions:
        if position['symbol'] == symbol and position['positionSide'] == position_side and float(position['positionAmt']) != 0:
            quantity = abs(float(position['positionAmt']))
            open_orders = get_open_orders(symbol, api_key, api_secret)

            if open_orders is None:
                print("Failed to get open orders.")
                return

            side = 'SELL' if position_side == 'LONG' else 'BUY'
            has_stop_loss_order = any(order['type'] == 'STOP_MARKET' and order['side'] == side and order['positionSide'] == position_side for order in open_orders)
            print(f"Has stop loss order: {has_stop_loss_order}")

            if not has_stop_loss_order:
                print(f"No stop loss order for {position_side} side detected, opening one...")
                response = open_stop_loss_order(symbol, side, quantity, stop_loss_price, api_key, api_secret, position_side)
                print("Stop loss order response:", response)
                logger.info(f"Stop loss order opened: {response}")
            else:
                print(f"Stop loss order for {position_side} side already exists.")

def open_take_profit_order(symbol, side, quantity, take_profit_price, api_key, api_secret, position_side):
    """Open a take profit order."""
    print(f"Opening take profit order for {position_side}...")
    endpoint = '/fapi/v1/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'side': side,
        'type': 'TAKE_PROFIT_MARKET',
        'quantity': round(quantity, 3),  # Round to 3 decimal places
        'stopPrice': round(take_profit_price, 2),  # Round to 2 decimal places
        'timestamp': timestamp,
        'positionSide': position_side,
        'workingType': working_type
    }

    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    signature = create_signature(query_string, api_secret)
    params['signature'] = signature

    headers = {
        'X-MBX-APIKEY': api_key
    }

    response = requests.post(base_url + endpoint, headers=headers, data=params)
    print(f"Take profit order response: {response.json()}")
    return response.json()

def check_and_set_take_profit(symbol, position_side, api_key, api_secret):
    """Check if a take profit order exists for a position, and create one if it doesn't."""
    positions = get_positions(api_key, api_secret)
    market_price = get_market_price(symbol, api_key, api_secret)
    
    # Calculate take profit price based on leverage and ROI
    take_profit_price = market_price * (1 + take_profit_roi / leverage / 100) if position_side == 'LONG' else market_price * (1 - take_profit_roi / leverage / 100)

    if market_price is None:
        print("Error: Could not retrieve market price.")
        return

    for position in positions:
        if position['symbol'] == symbol and position['positionSide'] == position_side and float(position['positionAmt']) != 0:
            quantity = abs(float(position['positionAmt']))
            open_orders = get_open_orders(symbol, api_key, api_secret)

            if open_orders is None:
                print("Failed to get open orders.")
                return

            side = 'SELL' if position_side == 'LONG' else 'BUY'
            has_take_profit_order = any(order['type'] == 'TAKE_PROFIT_MARKET' and order['side'] == side and order['positionSide'] == position_side for order in open_orders)
            print(f"Has take profit order: {has_take_profit_order}")

            if not has_take_profit_order:
                print(f"No take profit order for {position_side} side detected, opening one...")
                response = open_take_profit_order(symbol, side, quantity, take_profit_price, api_key, api_secret, position_side)
                print("Take profit order response:", response)
                logger.info(f"Take profit order opened: {response}")
            else:
                print(f"Take profit order for {position_side} side already exists.")



def manage_orders(api_key, api_secret, symbol, missing_side):
    print(f"Managing orders for {missing_side}...")

    # Muuta vivutus ja margin tyyppi
    change_leverage(symbol, leverage, api_key, api_secret)
    change_margin_type(symbol, margin_type, api_key, api_secret)

    # Laske vivutettu määrä
    leveraged_quantity = order_quantity * leverage
    print(f"Leveraged quantity: {leveraged_quantity}")

    # Tarkistetaan avoimet tilaukset
    open_orders = get_open_orders(symbol, api_key, api_secret)
    if open_orders is None:
        print("Failed to get open orders.")
        return

    # Tarkistetaan, onko jo olemassa trailing stop -tilauksia
    side = 'BUY' if missing_side == 'LONG' else 'SELL'
    position_side = missing_side
    has_trailing_stop_order = any(order['type'] == 'TRAILING_STOP_MARKET' and order['side'] == side and order['positionSide'] == position_side for order in open_orders)
    print(f"Has trailing stop order: {has_trailing_stop_order}")

    if not has_trailing_stop_order:
        print(f"No trailing stop order for {missing_side} side detected, opening one...")
        response = open_trailing_stop_order(symbol, side, leveraged_quantity, callback_rate, api_key, api_secret, missing_side, working_type)
        print("Trailing stop order response:", response)
    else:
        print(f"Trailing stop order for {missing_side} side already exists.")


   




