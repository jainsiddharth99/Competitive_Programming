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


def maxSlidingWindow2(nums: list[int], k: int) -> list[int]:
    q = deque()
    res = []
    l = r = 0
    n = len(nums)
    while r < n:
        while q and nums[q[-1]] <= nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if r+1 >= k:
            res.append(nums[q[0]])
            l += 1
        r += 1
    return res


nums = [8, 7, 6, 9]
print(maxSlidingWindow2(nums, 2))

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
