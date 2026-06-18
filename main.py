import time

from price_fetcher import get_price
from alert import check_alert
from notification import play_alert, show_notification
from telegram_notification import send_telegram_message
from logger import log_message

target = float(input("Enter target price: "))

log_message(f"BOT STARTED | Target={target}")

alert_sent = False

try:

    while True:

        try:

            price = get_price()

        except Exception as e:

            log_message(f"PRICE FETCH ERROR | {e}")

            print(f"Price Error: {e}")

            time.sleep(30)

            continue

        print(f"Current Price: {price}")

        if check_alert(price, target) and not alert_sent:

            log_message(
                f"ALERT TRIGGERED | Price={price} | Target={target}"
            )

            play_alert()

            show_notification(price, target)

            message = f"""
🚨 BTC ALERT 🚨

Current Price: {price}
Target Price: {target}
"""

            try:

                send_telegram_message(message)

                log_message("TELEGRAM MESSAGE SENT")

            except Exception as e:

                log_message(f"TELEGRAM ERROR | {e}")

                print(f"Telegram Error: {e}")

            print("Alert Triggered")

            alert_sent = True

        time.sleep(10)

except KeyboardInterrupt:

    log_message("BOT STOPPED BY USER")

    print("\nBot Stopped")