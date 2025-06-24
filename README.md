 📈 Crypto Trading Bot using Python & Binance API

Features

 ✅ Connects to Binance Futures Testnet using `python-binance`
 ✅ Supports Market and Limit orders
 ✅ Interactive Command-Line Interface (CLI)
 ✅ Real-time logging of trades
 ✅ Customizable with `.env` API keys
 ✅ Optional React Dashboard for monitoring (frontend folder)
 ✅ Ready for deployment on Vercel (UI)

 🛠️ Tech Stack

 Python 3.x
 `python-binance` library
 Binance Futures Testnet
 CLI for user interaction
 React (for optional frontend)
 Vercel (for optional frontend hosting)

Set up your .env file
Create a .env file in the root directory and add:
API_KEY=your_api_key_here
API_SECRET=your_secret_key_here
 Usage
Run the trading bot:

bash
Copy
Edit
python main.py
You will be prompted to:

Choose an order type (Market / Limit)

Enter symbol (e.g., BTCUSDT)
Enter quantity
Enter price (for Limit orders)

 Frontend (Optional)
now you can use the provided React frontend:
cd frontend
npm install
npm run build

👨‍💻 Author
Created by spati10
