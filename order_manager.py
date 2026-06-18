import time
import json
import hmac
import hashlib
import requests

from config import (
    COINDCX_API_KEY,
    COINDCX_SECRET_KEY
)


def place_order(
    market,
    side,
    order_type,
    quantity,
    price=None
):

    secret_bytes = bytes(
        COINDCX_SECRET_KEY,
        encoding="utf-8"
    )

    payload = {
        "side": side,
        "order_type": order_type,
        "market": market,
        "total_quantity": quantity,
        "timestamp": int(
            round(time.time() * 1000)
        )
    }

    if price is not None:

        payload["price_per_unit"] = price

    json_body = json.dumps(
        payload,
        separators=(",", ":")
    )

    signature = hmac.new(
        secret_bytes,
        json_body.encode(),
        hashlib.sha256
    ).hexdigest()

    headers = {
        "Content-Type": "application/json",
        "X-AUTH-APIKEY": COINDCX_API_KEY,
        "X-AUTH-SIGNATURE": signature
    }

    response = requests.post(
        "https://api.coindcx.com/exchange/v1/orders/create",
        data=json_body,
        headers=headers
    )

    return response.json()


def place_market_buy(
    market,
    quantity
):

    return place_order(
        market=market,
        side="buy",
        order_type="market_order",
        quantity=quantity
    )


def place_market_sell(
    market,
    quantity
):

    return place_order(
        market=market,
        side="sell",
        order_type="market_order",
        quantity=quantity
    )


def place_limit_buy(
    market,
    quantity,
    price
):

    return place_order(
        market=market,
        side="buy",
        order_type="limit_order",
        quantity=quantity,
        price=price
    )


def place_limit_sell(
    market,
    quantity,
    price
):

    return place_order(
        market=market,
        side="sell",
        order_type="limit_order",
        quantity=quantity,
        price=price
    )