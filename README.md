# FuturesBot
USE AT YOUR OWN RISK!!!

# Binance Futures Trading Bot

This is a Binance Futures trading bot designed to automate the process of managing stop loss, trailing stop, and take profit orders based on predefined parameters. The bot continuously monitors open positions and ensures that appropriate risk management orders are in place. In the config.py file, you can define various parameters, such as the leverage and margin type that are common to all traded symbols (coin pairs). Multiple different symbols can be in operation, for which you can set parameters like callback rates for openings and closings, as well as stop loss and take profit percentages. You can also specify whether you use static stop loss and take profit orders or dynamic trailing stop orders for each symbol. You can start testing the bot on Binance's futures test network by configuring the bot to use it.

## Features

- **Automated Order Management**: Automatically places stop loss, trailing stop, and take profit orders for open positions.
- **Leverage and Margin Type Adjustment**: Supports changing leverage and margin type for the specified trading symbol.
- **Logging**: Logs all significant events and actions to a file for easy tracking and debugging.

## Requirements

- Python 3.6+
- Binance Futures API Key and Secret

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/FuturesBot.git
    cd FuturesBot
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure API Keys and Parameters:**

    Create a `config.py` file in the root directory of the project with the following content:

    ```python
# API Credentials
api_key = 'YOUR_API_KEY'  # Binance API Key
api_secret = 'YOUR_API_SECRET'  # Binance API Secret

# Testnet URL
base_url = 'https://testnet.binancefuture.com'  # URL for Binance Futures Testnet

# Production URL (uncomment this line if you want to use the production environment)
#base_url = 'https://fapi.binance.com'  # URL for Binance Futures Production

# Settings
leverage = 10  # Leverage to use for the positions. Can vary between 1-125 depending on the symbol. Adjust this setting based on your risk management decision.
margin_type = 'ISOLATED'  # Margin type: ISOLATED or CROSSED

# Cryptocurrency-specific settings. You can add multiple symbols using this template.
crypto_settings = {
    "BTCUSDT": {
        "order_quantity": 0.0002,     # Order quantity in BTC
        "callback_rate": 0.5,         # Callback rate percentage for trailing stop order
        "callback_rate_close": 0.3,   # Callback rate percentage for closing trailing stop order
        "working_type": "MARK_PRICE", # Working type can be 'MARK_PRICE' or 'LAST_PRICE'
        "stop_loss_roi": -30,         # Stop loss return on investment percentage
        "take_profit_roi": 40,        # Take profit return on investment percentage
        "take_profit_enabled": False, # If True, set a take profit order instead of a trailing stop close order
    }
}

    ```

## Usage

1. **Run the Bot:**

    ```bash
    python main.py
    ```

2. **Monitor the Logs:**

    The bot logs all activities to `order_management.log`. You can monitor this file to track the bot's actions and any errors that may occur.

## Functions

- **main_loop**: The main loop that keeps bot up and running.
- **check_and_set_stop_loss**: Checks if a stop loss order exists and places one if it doesn't.
- **check_and_set_take_profit**: Checks if a take profit order exists and places one if it doesn't.
- **open_trailing_stop_order**: Places a trailing stop order either for opening or closing.
- **open_stop_loss_order**: Places a stop loss order.
- **open_take_profit_order**: Places a take profit order.
- **change_leverage**: Changes the leverage for the specified symbol. Done only once when the bot is started. Restart is required if you want to change this. Common for all symbols.
- **change_margin_type**: Changes the margin type for the specified symbol.
- **get_open_orders**: Retrieves the list of open orders.
- **get_market_price**: Retrieves the current market price of the specified symbol.
- **get_positions**: Retrieves the current positions.
