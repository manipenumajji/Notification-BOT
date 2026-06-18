from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from config import TELEGRAM_BOT_TOKEN

from portfolio import get_portfolio_report

from coindcx_client import (
    get_balance,
    get_trade_history,
    get_price
)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        """
Available Commands:

/portfolio
/balance
/trades
/price coin
"""
    )


async def portfolio(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    report = get_portfolio_report()

    await update.message.reply_text(
        report
    )


async def balance(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    balances = get_balance()

    message = "💰 BALANCES\n\n"

    for item in balances:

        if item["balance"] > 0:

            message += (
                f'{item["currency"]}: '
                f'{item["balance"]:.5f}\n'
            )

    await update.message.reply_text(
        message
    )


async def trades(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    trade_history = get_trade_history()

    latest_trade = trade_history[-1]

    message = f"""
📈 LAST TRADE

Symbol: {latest_trade["symbol"]}
Side: {latest_trade["side"]}
Price: {latest_trade["price"]}
Quantity: {latest_trade["quantity"]}
"""

    await update.message.reply_text(
        message
    )


async def price(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if len(context.args) == 0:

        await update.message.reply_text(
            "Usage:\n/price BTCINR"
        )

        return

    coin = context.args[0].upper()
    market = coin + "INR"

    try:

        current_price = get_price(
            market
        )

        message = f"""
💲 {coin}

Current Price: ₹{current_price}
"""

        await update.message.reply_text(
            message
        )

    except Exception as e:

        await update.message.reply_text(
            str(e)
        )


app = Application.builder().token(
    TELEGRAM_BOT_TOKEN
).build()


app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

app.add_handler(
    CommandHandler(
        "portfolio",
        portfolio
    )
)

app.add_handler(
    CommandHandler(
        "balance",
        balance
    )
)

app.add_handler(
    CommandHandler(
        "trades",
        trades
    )
)

app.add_handler(
    CommandHandler(
        "price",
        price
    )
)


print("Telegram Bot Running...")

app.run_polling()