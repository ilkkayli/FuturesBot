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


