from dotenv import load_dotenv
import os
load_dotenv()
COINDCX_API_KEY=os.getenv("COINDCX_API_KEY")
COINDCX_SECRET_KEY=os.getenv("COINDCX_SECRET_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
if not COINDCX_API_KEY:
    raise ValueError("COINDCX_API_KEY is missing")
if not COINDCX_SECRET_KEY:
    raise ValueError("COINDCX_SECRET_KEY is missing")