import time
from order_management import handle_orders  # Import the handle_orders function from the order_management module
from config import crypto_settings  # Import the crypto_settings dictionary from the config module

# Infinite loop to continuously check and manage orders
while True:
    # Iterate through each symbol and its parameters in the crypto_settings dictionary
    for symbol, params in crypto_settings.items():
        # Extract individual parameters for the current symbol
        order_quantity = params["order_quantity"]  # The order quantity for the symbol
        callback_rate = params["callback_rate"]  # The callback rate for the trailing stop order
        callback_rate_close = params["callback_rate_close"]  # The callback rate for closing the trailing stop order
        working_type = params["working_type"]  # The type of price to use ('MARK_PRICE' or 'LAST_PRICE')
        stop_loss_roi = params["stop_loss_roi"]  # The stop loss return on investment percentage
        take_profit_roi = params["take_profit_roi"]  # The take profit return on investment percentage
        take_profit_enabled = params["take_profit_enabled"]  # Whether to enable take profit order instead of trailing stop close order
        
        # Call the handle_orders function with the extracted parameters
        handle_orders(symbol, order_quantity, callback_rate, callback_rate_close, working_type, stop_loss_roi, take_profit_roi, take_profit_enabled)
    
    # Sleep for xx seconds before the next iteration to avoid overwhelming the API with requests. You can adjust this starting from 1 second.
    time.sleep(10)




