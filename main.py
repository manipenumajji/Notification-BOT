import time

from price_fetcher import get_price
from alert import check_alert
from notification import play_alert, show_notification
from telegram_notification import send_telegram_message

target = float(input("Enter target price: "))

alert_sent = False

while True:

    price = get_price()

    print(f"Current Price: {price}")

    if check_alert(price, target) and not alert_sent:

        play_alert()

        show_notification(price, target)

        message = f"""
🚨 BTC ALERT 🚨

Current Price: {price}
Target Price: {target}
"""

        send_telegram_message(message)

        print("Alert Triggered")

        alert_sent = True

    time.sleep(10)