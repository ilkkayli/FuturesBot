import time
from binance_futures import check_if_positions_exist
from order_management import manage_orders, check_and_set_stop_loss, check_and_set_take_profit
from config import api_key, api_secret, symbol

def main_loop():
    while True:
        print("Starting new loop iteration...")
        has_long, has_short = check_if_positions_exist(symbol)

        if has_long:
            check_and_set_stop_loss(symbol, 'LONG', api_key, api_secret)
            check_and_set_take_profit(symbol, 'LONG', api_key, api_secret)
        else:
            print("No LONG position detected, managing orders...")
            manage_orders(api_key, api_secret, symbol, 'LONG')

        if has_short:
            check_and_set_stop_loss(symbol, 'SHORT', api_key, api_secret)
            check_and_set_take_profit(symbol, 'SHORT', api_key, api_secret)
        else:
            print("No SHORT position detected, managing orders...")
            manage_orders(api_key, api_secret, symbol, 'SHORT')

        time.sleep(10)

if __name__ == '__main__':
    main_loop()


