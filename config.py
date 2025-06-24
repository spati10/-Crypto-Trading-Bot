import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

TESTNET_URL = "https://testnet.binancefuture.com"

print("API_KEY:", API_KEY)
print("API_SECRET:", API_SECRET)
