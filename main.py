from bot import BasicBot
from binance.enums import *
import sys

def main():
    bot = BasicBot()
    
    print("=== Binance Futures Testnet Trading Bot ===")
    print("Choose Order Type:")
    print("1. Market Order")
    print("2. Limit Order")
    print("3. Stop-Limit Order (Bonus)")

    choice = input("Enter choice (1/2/3): ").strip()
    
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").strip().upper()
    side_input = input("Buy or Sell? ").strip().lower()
    side = SIDE_BUY if side_input == 'buy' else SIDE_SELL
    quantity = float(input("Enter quantity (e.g., 0.001): "))

    if choice == '1':
        result = bot.place_market_order(symbol, side, quantity)
    elif choice == '2':
        price = input("Enter limit price (e.g., 25000): ").strip()
        result = bot.place_limit_order(symbol, side, quantity, price)
    elif choice == '3':
        stop_price = input("Enter stop price (e.g., 24000): ").strip()
        result = bot.place_stop_limit_order(symbol, side, quantity, stop_price, stop_price)
    else:
        print("Invalid choice.")
        sys.exit(1)

    if result:
        print("Order executed successfully!")
        print(result)
    else:
        print("Order failed. Check logs for details.")

if __name__ == '__main__':
    main()
