def totalSteps(nums: list[int]) -> int:
    n = len(nums)
    s = []
    dp = [0]*n
    for i in range(n-1, -1, -1):
        while s and nums[i] > nums[s[-1]]:
            dp[i] = max(dp[i]+1, dp[s.pop()])
        s.append(i)
    return max(dp)


nums = [10, 1, 2, 3, 4, 5, 6, 1, 2, 3]
print(totalSteps(nums))
