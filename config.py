<<<<<<< HEAD
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

# Explanation of each setting:
# api_key: Your Binance API key.
# api_secret: Your Binance API secret key.
# base_url: The base URL for the Binance Futures API. Use the testnet URL for testing and the production URL for real trading.
# leverage: The leverage level you want to use for trading.
# margin_type: The type of margin you want to use ('ISOLATED' or 'CROSSED').
# crypto_settings: A dictionary containing specific settings for different cryptocurrency pairs.
#   - order_quantity: The amount of the cryptocurrency you want to trade.
#   - callback_rate: The callback rate percentage for the trailing stop order (when it opens).
#   - callback_rate_close: The callback rate percentage for the trailing stop order (when it closes).
#   - working_type: The type of price to use for the order ('MARK_PRICE' or 'LAST_PRICE').
#   - stop_loss_roi: The percentage loss at which a stop loss order should be triggered to be divided by the leverage.
#   - take_profit_roi: The percentage gain at which a take profit order should be triggered to be diveded by the leverage.
#   - take_profit_enabled: If set to True, a take profit order will be set instead of a trailing stop close order.


=======
# API-tunnukset
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Testnet URL
base_url = 'https://testnet.binancefuture.com'

# Tuotantoympäristön URL (jos haluat käyttää tuotantoa, muuta base_url tähän)
# base_url = 'https://fapi.binance.com'

# Asetukset
symbol = 'BTCUSDT'  # Default symboli
leverage = 15
margin_type = 'ISOLATED'
order_quantity = 0.01  # Alustava määrä, joka vivutetaan leverage-arvolla
callback_rate = 1.0  # Trailing stop callback rate (esimerkkinä 1%)
working_type = 'MARK_PRICE'  # Voit valita joko 'MARK_PRICE' tai 'CONTRACT_PRICE'
stop_loss_roi = -5  # ROI% for stop loss, to be divided by leverage
take_profit_roi = 10  # Take profit ROI as a percentage, to be divided by leverage


>>>>>>> c583115c0c7a00e55126e5566ba9834a94730215
