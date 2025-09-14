# Crypto-Trading-Bot

# Binance Futures Simplified Trading Bot

## Overview
This project is a simplified Python trading bot for **Binance Futures Testnet (USDT-M)**.  
It supports **market** and **limit** orders for both **BUY** and **SELL** sides, with full logging and error handling.  

The bot is designed for **reusability**, **clear input/output handling**, and can be extended to advanced order types (Stop-Limit, OCO, TWAP, Grid).

---

## Features

- Place **MARKET** and **LIMIT** orders on Binance Futures Testnet  
- Supports both **BUY** and **SELL**  
- Command-line interface (CLI) for interactive trading  
- Logs API requests, responses, and errors  
- Structured code for **reusability**  
- Optional: Easy to extend for advanced order types  

---

## Requirements

- Python 3.10+  
- `python-binance` library  

Install dependencies:

```bash
pip install -r requirements.txt
```
# Setup
- Register on Binance Futures Testnet: https://testnet.binancefuture.com
- Generate API Key and Secret
- Update config.py with your API credentials:
```
API_KEY = 'your_testnet_api_key'
API_SECRET = 'your_testnet_api_secret'
TESTNET_URL = 'https://testnet.binancefuture.com'
```
# Project Structure
```
trading_bot/
│
├── config.py         # API credentials & testnet URL
├── bot.py            # Trading bot class with order methods
├── main.py           # CLI interface
├── logger.py         # Logging setup
├── requirements.txt  # Python dependencies
└── logs/
    └── bot.log       # API request/response log
```
# Usage
Run the CLI:
`python main.py`

Follow the prompts:
```
Enter symbol (e.g., BTCUSDT): BTCUSDT
Order Side (BUY or SELL): BUY
Order Type (MARKET or LIMIT): MARKET
Quantity (e.g., 0.001): 0.001
```
For LIMIT orders, you will be prompted for a price:

`Limit Price (e.g., 30000): 30000`

The bot will place the order and output the order details:
```
Order placed successfully!
{'orderId': 123456789, 'symbol': 'BTCUSDT', ...}
```
All API interactions and errors are logged in logs/bot.log.
