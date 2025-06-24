import streamlit as st

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 330,
    "AMZN": 125
}

st.title("📈 Stock Portfolio Tracker")
st.markdown("Track your investments in popular stocks easily!")

# Step 2: User inputs
portfolio = {}

st.subheader("Select Stocks and Quantity")
for stock in stock_prices:
    qty = st.number_input(f"Quantity of {stock} (${stock_prices[stock]} per share)", min_value=0, step=1)
    if qty > 0:
        portfolio[stock] = qty

# Step 3: Calculate total investment
if st.button("Generate Portfolio Summary"):
    if portfolio:
        total_investment = 0
        st.subheader("📊 Portfolio Summary")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            total_investment += investment
            st.write(f"**{stock}**: {qty} shares × ${price} = **${investment}**")

        st.success(f"💰 Total Investment: **${total_investment}**")

        # Step 4: Option to download the summary
        summary = "Stock Portfolio Summary:\n"
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            summary += f"{stock}: {qty} shares × ${price} = ${investment}\n"
        summary += f"\nTotal Investment: ${total_investment}"

        st.download_button("📥 Download Summary", summary, file_name="portfolio_summary.txt")
    else:
        st.warning("Please select at least one stock.")
