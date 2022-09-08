def lengthOfLIS(nums: list[int]) -> int:
    # n = len(nums)
    # dp = [1]*n
    # for i in range(n-2, -1, -1):
    #     for j in range(i+1, n):

    #         if nums[i] < nums[j]:
    #             dp[i] = max(dp[i], 1+dp[j])

    # return max(dp)
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size


nums = [0, 1, 0, 3, 2, 3]

print(lengthOfLIS(nums))
"""
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
"""
