from bot import BasicBot

def get_user_input():
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    side = input("Buy or Sell? (buy/sell): ").lower()
    order_type = input("Order type? (market/limit): ").lower()
    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == "limit":
        price = float(input("Enter limit price: "))

    return symbol, side, order_type, quantity, price

def main():
    bot = BasicBot()
    symbol, side, order_type, quantity, price = get_user_input()
    bot.place_order(symbol, side, order_type, quantity, price)

if __name__ == "__main__":
    main()
