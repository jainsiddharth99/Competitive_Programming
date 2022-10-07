from collections import deque


def constrainedSubsetSum(nums: list[int], k: int) -> int:
    n = len(nums)
    dp = [0]*n
    q = deque()

    for i, num in enumerate(nums):
        if i > k and q[0] == dp[i-k-1]:
            q.popleft
        dp[i] = max(q[0] if q else 0, 0)+num

        while q and q[-1] < dp[i]:
            q.pop()
        q.append(dp[i])
    return max(dp)


nums = [10, 2, -10, 5, 20]
print(constrainedSubsetSum(nums, 2))


"""
Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
 
"""
