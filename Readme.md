USE AT YOUR OWN RISK!!!

# Binance Futures Trading Bot

This is a Binance Futures trading bot designed to automate the process of managing stop loss, trailing stop, and take profit orders based on predefined parameters. The bot continuously monitors open positions and ensures that appropriate risk management orders are in place. The bot's strategy is to detect clear trend changes in the price and make investment decisions accordingly. The strategy can be adjusted through the parameters in the config.py file, where you can, for example, modify the take profit and stop loss levels according to your own risk tolerance. Similarly, you can adjust the leverage used.

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
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    base_url = 'https://fapi.binance.com'
    leverage = 20  # Set your desired leverage
    margin_type = 'ISOLATED'  # or 'CROSSED'
    order_quantity = 0.001  # Set your desired order quantity
    symbol = 'BTCUSDT'  # Set your desired trading symbol
    callback_rate = 1.0  # Set your desired trailing stop callback rate
    working_type = 'MARK_PRICE'  # or 'CONTRACT_PRICE'
    stop_loss_roi = 2.0  # Stop loss ROI percentage
    take_profit_roi = 10.0  # Take profit ROI percentage
    ```

## Usage

1. **Run the Bot:**

    ```bash
    python main.py
    ```

2. **Monitor the Logs:**

    The bot logs all activities to `order_management.log`. You can monitor this file to track the bot's actions and any errors that may occur.

## Functions

- **main_loop**: The main loop that continuously checks for positions and manages orders.
- **check_and_set_stop_loss**: Checks if a stop loss order exists and places one if it doesn't.
- **check_and_set_take_profit**: Checks if a take profit order exists and places one if it doesn't.
- **open_trailing_stop_order**: Places a trailing stop order.
- **open_stop_loss_order**: Places a stop loss order.
- **open_take_profit_order**: Places a take profit order.
- **change_leverage**: Changes the leverage for the specified symbol.
- **change_margin_type**: Changes the margin type for the specified symbol.
- **get_open_orders**: Retrieves the list of open orders.
- **get_market_price**: Retrieves the current market price of the specified symbol.
- **get_positions**: Retrieves the current positions.


