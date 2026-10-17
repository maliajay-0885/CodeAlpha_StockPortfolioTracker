
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 165,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("Stock Portfolio Tracker")
print("-----------------------")
print("Available stocks:")
for symbol, price in stock_prices.items():
    print(f"{symbol}: ${price} per share")

while True:
    symbol = input("\nEnter stock symbol (or DONE to finish): ").strip().upper()

    if symbol == "DONE":
        break

    if symbol not in stock_prices:
        print("Invalid stock symbol. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[symbol]
    investment = price * quantity
    total_investment += investment

    portfolio.append((symbol, quantity, price, investment))

    print(f"{quantity} shares of {symbol} = ${investment}")

print("\n----- Portfolio Summary -----")

if not portfolio:
    print("No stocks were added.")
else:
    for symbol, quantity, price, investment in portfolio:
        print(f"{symbol}: {quantity} shares x ${price} = ${investment}")

    print(f"\nTotal Investment: ${total_investment}")

    with open("portfolio.txt", "w", encoding="utf-8") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")

        for symbol, quantity, price, investment in portfolio:
            file.write(
                f"{symbol}: {quantity} shares x ${price} = ${investment}\n"
            )

        file.write(f"\nTotal Investment: ${total_investment}\n")

    print("Portfolio saved to portfolio.txt")

print("\nThank you for using Stock Portfolio Tracker!")
