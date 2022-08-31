def maxProfit(prices):
    # profit = 0
    # n = len(prices)
    # buy = prices[0]
    # for i in range(n):
    #     profit = max(profit, prices[i]-buy)
    #     buy = min(buy, prices[i])

    # return profit

    # 2nd try
    profit = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        profit = max(profit, prices[i]-buy)
        buy = min(buy, prices[i])

    return profit

    # buy, ans = float('inf'), 0
    # for p in prices:
    # 	buy, ans = min(buy, p), max(ans, p-buy)
    # return ans


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))


"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
