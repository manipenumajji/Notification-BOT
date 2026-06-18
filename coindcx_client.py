import time
import json
import hmac
import hashlib
import requests

from config import COINDCX_API_KEY
from config import COINDCX_SECRET_KEY


def get_price():

    url = "https://api.coindcx.com/exchange/ticker"

    response = requests.get(url)

    data = response.json()

    for item in data:

        if item["market"] == "BTCUSDT":

            return float(item["last_price"])

    raise Exception("BTCUSDT market not found")


def make_authenticated_request(endpoint):

    secret_bytes = bytes(
        COINDCX_SECRET_KEY,
        encoding="utf-8"
    )

    payload = {
        "timestamp": int(round(time.time() * 1000))
    }

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
        "X-AUTH-APIKEY": COINDCX_API_KEY,
        "X-AUTH-SIGNATURE": signature
    }

    url = f"https://api.coindcx.com/exchange/v1/users/{endpoint}"

    response = requests.post(
        url,
        data=json_body,
        headers=headers
    )

    return response.json()


def get_balance():

    return make_authenticated_request("balances")
#orders we placed
def get_orders():

    secret_bytes = bytes(
        COINDCX_SECRET_KEY,
        encoding="utf-8"
    )

    payload = {
        "timestamp": int(round(time.time() * 1000))
    }

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
        "X-AUTH-APIKEY": COINDCX_API_KEY,
        "X-AUTH-SIGNATURE": signature
    }

    response = requests.post(
        "https://api.coindcx.com/exchange/v1/orders/active_orders",
        data=json_body,
        headers=headers
    )

    return response.json()
#trading history 
def get_trade_history():

    secret_bytes = bytes(
        COINDCX_SECRET_KEY,
        encoding="utf-8"
    )

    payload = {
        "timestamp": int(round(time.time() * 1000))
    }

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
        "X-AUTH-APIKEY": COINDCX_API_KEY,
        "X-AUTH-SIGNATURE": signature
    }

    response = requests.post(
        "https://api.coindcx.com/exchange/v1/orders/trade_history",
        data=json_body,
        headers=headers
    )

    return response.json()