prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150
}

portfolio = {}

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock (DONE to stop): ").upper()

    if stock == "DONE":
        break

    if stock in prices:
        quantity = int(input("Enter quantity: "))

        portfolio[stock] = quantity

    else:
        print("Stock not available!")

total = 0

print("\nYour Portfolio:")

for stock in portfolio:
    value = prices[stock] * portfolio[stock]

    print(stock, ":", value)

    total = total + value

print("Total Investment:", total)

with open("portfolio.txt", "w") as file:
    file.write("Total Investment: " + str(total))

print("Report Saved!")