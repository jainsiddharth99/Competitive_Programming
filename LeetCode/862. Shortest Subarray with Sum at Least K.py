from collections import deque


def shortestSubarray(nums: list[int], k: int) -> int:
    pre = [0]
    for i in nums:
        pre.append(pre[-1]+i)
    n = len(nums)
    q = deque()
    res = n+1
    for i, val in enumerate(pre):
        while q and val <= pre[q[-1]]:
            q.pop()
        while q and val-pre[q[0]] >= k:
            res = min(res, i-q.popleft())
        q.append(i)

    return res if res < n+1 else -1


nums = [2, -1, 2]
print(shortestSubarray(nums, 3))

"""
Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
"""
