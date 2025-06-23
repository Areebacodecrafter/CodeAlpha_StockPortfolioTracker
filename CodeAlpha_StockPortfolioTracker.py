# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 330,
    "AMZN": 125
}

# Step 2: User inputs
print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", list(stock_prices.keys()))

portfolio = {}  # to store user's stocks and quantities

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Please choose from the available list.")
        continue
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        if qty < 0:
            print("Quantity cannot be negative.")
            continue
        portfolio[stock] = qty
    except ValueError:
        print("❌ Please enter a valid number for quantity.")

# Step 3: Calculate total investment
print("\n📊 Portfolio Summary:")
total_investment = 0
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment: ${total_investment}")

# Step 4: Save to a text file (optional)
save = input("Do you want to save this summary to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${investment}\n")
        file.write(f"\nTotal Investment: ${total_investment}")
    print("✅ Summary saved to 'portfolio_summary.txt'")
