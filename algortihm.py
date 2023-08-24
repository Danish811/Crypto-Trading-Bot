import Connect
curr = 0
highest = 0
lowest = 0

if lows[i] < closes[i - 1] and closes[i] > closes[i - 1]:
    Connect.OrderBuy()

if highs[i] > closes[i - 1] and closes[i] < closes[i - 1]:
    Connect.OrderSell()