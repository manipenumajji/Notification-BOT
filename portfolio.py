from coindcx_client import get_balance
from coindcx_client import get_price


def get_portfolio_report():

    balances = get_balance()

    total_value = 0

    report = "📊 PORTFOLIO REPORT\n\n"

    for item in balances:

        balance = item["balance"]

        currency = item["currency"]

        if balance <= 0:

            continue

        if currency == "INR":

            value = balance

        else:

            market = currency + "INR"

            price = get_price(market)

            value = balance * price

        report += (
            f"{currency} | Qty: {balance:.8f} | "
            f"Value: ₹{value:.2f}\n"
        )

        total_value += value

    report += (
        f"\n------------------\n"
        f"Total Portfolio Value: ₹{total_value:.2f}"
    )

    return report