from bot.client import get_client
from bot.logging_config import logger
from binance.exceptions import BinanceAPIException


def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    params = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    try:
        logger.info(f"API Request: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"API Response: {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise