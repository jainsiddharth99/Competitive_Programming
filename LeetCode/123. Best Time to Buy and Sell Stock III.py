def maxprofit(prices):

    curr_profit = 0
    profit = []
    buy = prices[0]

    for i in prices:
        buy = min(buy, i)
        curr_profit = max(curr_profit, i-buy)
        profit.append(curr_profit)

    curr_profit = 0
    total = 0
    curr_max = prices[-1]

    for i in range(len(prices)-1, -1, -1):
        curr_max = max(curr_max, prices[i])
        curr_profit = max(curr_profit, curr_max-prices[i])
        total = max(total, curr_profit+profit[i])

    return total
    # profit.sort()
    # if len(profit) > 1:
    #     return sum(profit[-2:])

    # else:
    #     return profit[-1]


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(maxprofit(prices))

"""
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
"""
