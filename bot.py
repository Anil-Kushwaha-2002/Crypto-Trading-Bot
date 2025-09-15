from binance.client import Client
from binance.enums import *
from logger import log_info, log_error
from config import API_KEY, API_SECRET, BASE_URL

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        self.client.FUTURES_URL = BASE_URL

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )
            log_info(f"Market order placed: {order}")
            return order
        except Exception as e:
            log_error(f"Market order error: {str(e)}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            log_info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            log_error(f"Limit order error: {str(e)}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_STOP_MARKET,
                stopPrice=stop_price,
                quantity=quantity
            )
            log_info(f"Stop limit order placed: {order}")
            return order
        except Exception as e:
            log_error(f"Stop limit order error: {str(e)}")
            return None

