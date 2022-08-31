def maxprofit(prices):
    curr_profit = 0
    profit = 0
    buy = prices[0]

    for i in prices:
        curr_profit = i-buy
        if curr_profit > 0:
            buy = i
            profit += curr_profit
        buy = min(buy, i)

    return profit


prices = [1, 2, 3, 4, 5]
print(maxprofit(prices))


"""
Input: 
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""
