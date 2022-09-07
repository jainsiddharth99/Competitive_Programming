def rob(nums: list[int]) -> int:
    # rob1, rob2 = 0, 0

    # for n in nums:
    #     tmp = max(rob1+n, rob2)
    #     rob1 = rob2
    #     rob2 = tmp

    # return rob2

    # another one
    n = len(nums)
    dp = [0]*(n+1)

    dp[1] = nums[0]

    for i in range(1, n):
        dp[i+1] = max(dp[i], dp[i-1]+nums[i])

    return dp[n]


nums = [2, 7, 9, 3, 1]
print(rob(nums))
"""
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
