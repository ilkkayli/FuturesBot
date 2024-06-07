import logging
import os

LOG_DIR = "logs"

def setup_logger():
    # Luo lokituskansion, jos se ei ole jo olemassa
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # Määritä lokitustaso
    logging.basicConfig(level=logging.INFO)

def log_open_order(symbol, side, quantity, price, position_side, order_type):
    log_file = os.path.join(LOG_DIR, "orders.log")
    logger = logging.getLogger("order_logger")

    # Määritä lokitiedoston muotoilu
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Luo tiedostokäsittelijä lokitiedostolle
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Lisää tiedostokäsittelijä loggeriin
    logger.addHandler(file_handler)

    # Kirjoita lokimerkintä
    logger.info(f"Opened {order_type} order for {position_side}: Symbol={symbol}, Side={side}, Quantity={quantity}, Price={price}")

    # Poista tiedostokäsittelijä loggerista
    logger.removeHandler(file_handler)
