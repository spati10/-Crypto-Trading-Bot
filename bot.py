from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
from config import API_KEY, API_SECRET, TESTNET_URL
from logger import setup_logger

logger = setup_logger()

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = TESTNET_URL
        self.client.API_URL = TESTNET_URL
        logger.info("Binance Futures client initialized (Testnet).")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol,
                'side': SIDE_BUY if side == "buy" else SIDE_SELL,
                'type': ORDER_TYPE_MARKET if order_type == "market" else ORDER_TYPE_LIMIT,
                'quantity': quantity,
            }

            if order_type == "limit":
                params.update({
                    'price': price,
                    'timeInForce': TIME_IN_FORCE_GTC,
                })

            logger.info(f"Placing order: {params}")
            order = self.client.futures_create_order(**params)
            logger.info(f"Order placed: {order}")
            return order

        except BinanceAPIException as e:
            logger.error(f"API Error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
