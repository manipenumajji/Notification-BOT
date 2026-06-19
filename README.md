# 🚀 Notification-BOT

A cloud-hosted cryptocurrency monitoring and portfolio management bot built with Python, CoinDCX API, Telegram Bot API, and Railway.

This project provides real-time cryptocurrency prices, portfolio tracking, trade monitoring, and Telegram-based account management from anywhere.

---

## ✨ Features

### 📊 Portfolio Dashboard

View your complete CoinDCX portfolio directly from Telegram.

```text
/portfolio
```

Example:

```text
📊 PORTFOLIO REPORT

BTC | Qty: 0.005 | Value: ₹32000
AI  | Qty: 12.5  | Value: ₹26.75

------------------
Total Portfolio Value: ₹32026.75
```

---

### 💰 Balance Tracking

Fetch all available wallet balances.

```text
/balance
```

---

### 📈 Trade History

View the most recent executed trade.

```text
/trades
```

Example:

```text
📈 LAST TRADE

Symbol: ADAINR
Side: BUY
Price: ₹50.80
Quantity: 7.81
```

---

### 💲 Live Price Lookup

Get real-time prices for any supported CoinDCX market.

```text
/price BTC
/price XRP
/price AI
```

Example:

```text
💲 BTC

Current Price: ₹6,405,293
```

---

### 📋 Watchlist

Monitor your favorite cryptocurrencies.

```text
/watchlist
```

Example:

```text
📋 WATCHLIST

BTC: ₹6,405,293
AI: ₹2.14
SHIB: ₹0.00047
XRP: ₹114.84
```

---

### 🔔 Price Alert System

Monitor target prices and receive alerts when conditions are met.

Features:

* Custom target prices
* Continuous monitoring
* Telegram notifications
* Sound alerts (local version)

---

### ☁️ Cloud Deployment

The bot is deployed on Railway and runs independently of a local machine.

Benefits:

* 24/7 availability
* No need to keep laptop running
* Accessible from anywhere via Telegram

---

## 🛠 Tech Stack

### Backend

* Python

### APIs

* CoinDCX API
* Telegram Bot API

### Libraries

* requests
* python-telegram-bot
* python-dotenv
* plyer

### Hosting

* Railway

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
Notification-BOT/

├── coindcx_client.py
├── telegram_bot.py
├── portfolio.py
├── order_manager.py
├── trade_monitor.py
├── telegram_utils.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/manipenumajji/Notification-BOT.git
```

Move into the project directory:

```bash
cd Notification-BOT
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file and add:

```env
COINDCX_API_KEY=your_api_key
COINDCX_SECRET_KEY=your_secret_key
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

Never commit your real API keys to GitHub.

---

## ▶️ Running Locally

Start the Telegram bot:

```bash
python telegram_bot.py
```

---

## 🚧 Future Roadmap

* Profit & Loss Tracking
* Telegram Buy/Sell Commands
* Strategy Engine
* Automated Trading
* Risk Management System
* Multi-Coin Monitoring
* Trade Journaling
* Performance Analytics

---

## 📜 License

This project is intended for educational and personal use.

Always test thoroughly before enabling live trading functionality.
