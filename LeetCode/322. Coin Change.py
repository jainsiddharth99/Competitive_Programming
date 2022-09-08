def coinChange(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0
    dp = [amount+1]*(amount+1)
    dp[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1+dp[i-coin])
    return dp[amount] if dp[amount] != amount+1 else -1


coins = [1, 2, 5]
amount = 13
print(coinChange(coins, amount))
"""
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

"""
