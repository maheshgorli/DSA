def maxProfit(prices):
    l, r = 0, 1
    maxp = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            if profit > maxp:
                maxp = profit
        else:
            l = r

        r += 1

    return maxp

prices = [7, 1, 5, 3, 6, 4]

result = maxProfit(prices)
print("Maximum Profit:", result)