from coindcx_client import get_balance
from main import send_telegram_message

data = get_balance()

message = "📊 PORTFOLIO REPORT\n\n"

for item in data:

    if item["balance"] > 0:

        message += (
            f"{item['currency']} : "
            f"{item['balance']:.8f}\n"
        )

print(message)
send_telegram_message(message)