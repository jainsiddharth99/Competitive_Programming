from collections import deque


from collections import deque


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    q = deque()
    res = []
    for i in range(len(nums)):
        while q and nums[q[-1]] <= nums[i]:
            q.pop()
        q.append(i)
        if q[0] == i-k:
            q.popleft()
        res.append(nums[q[0]])

    return res[k-1:]


nums = [1, 3, -1, -3, 5, 3, 6, 7]
print(maxSlidingWindow(nums, 3))

"""
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
