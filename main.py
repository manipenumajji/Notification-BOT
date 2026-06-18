import time
import winsound

from datetime import datetime
from plyer import notification

from coindcx_client import get_price
from telegram_utils import send_telegram_message


def log_message(message):

    current_time = datetime.now()

    with open("bot.log", "a") as file:

        file.write(
            f"{current_time} | {message}\n"
        )


def play_alert():

    winsound.Beep(1000, 1000)


def show_notification(price, target):

    notification.notify(
        title="Crypto Alert",
        message=f"BTC Price: {price}\nTarget: {target}",
        timeout=10
    )


target = float(
    input("Enter target price: ")
)

alert_sent = False

log_message(
    f"BOT STARTED | Target={target}"
)

try:

    while True:

        try:

            price = get_price("BTCUSDT")

        except Exception as e:

            log_message(
                f"PRICE FETCH ERROR | {e}"
            )

            print(
                f"Price Error: {e}"
            )

            time.sleep(30)

            continue

        print(
            f"Current Price: {price}"
        )

        if price >= target and not alert_sent:

            log_message(
                f"ALERT TRIGGERED | Price={price} | Target={target}"
            )

            play_alert()

            show_notification(
                price,
                target
            )

            message = f"""
🚨 BTC ALERT 🚨

Current Price: {price}
Target Price: {target}
"""

            try:

                send_telegram_message(
                    message
                )

                log_message(
                    "TELEGRAM MESSAGE SENT"
                )

            except Exception as e:

                log_message(
                    f"TELEGRAM ERROR | {e}"
                )

                print(
                    f"Telegram Error: {e}"
                )

            print(
                "Alert Triggered"
            )

            alert_sent = True

        time.sleep(10)

except KeyboardInterrupt:

    log_message(
        "BOT STOPPED BY USER"
    )

    print("\nBot Stopped")