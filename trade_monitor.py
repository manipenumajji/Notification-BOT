import time

from coindcx_client import get_trade_history
from telegram_utils import send_telegram_message
data = get_trade_history()

latest_trade = data[-1]

last_trade_id = latest_trade["id"]

print("Monitoring Started...")
print("Last Trade ID:", last_trade_id)
print("Checking every 60 seconds...")
while True:

    try:

        data = get_trade_history()

        latest_trade = data[-1]

        new_trade_id = latest_trade["id"]

        if new_trade_id != last_trade_id:

            message = f"""
✅ TRADE EXECUTED

Market: {latest_trade["symbol"]}
Side: {latest_trade["side"].upper()}
Price: {float(latest_trade["price"]):.2f}
Quantity: {float(latest_trade["quantity"]):.2f}
Fee: {latest_trade["fee_amount"]}
"""

            print(message)

            send_telegram_message(message)

            last_trade_id = new_trade_id

    except Exception as e:

        print("Monitor Error:", e)

    time.sleep(60)