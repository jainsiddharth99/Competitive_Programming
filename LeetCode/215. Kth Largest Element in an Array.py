import heapq
from multiprocessing import heap


def findKthLargest(nums: list[int], k: int) -> int:
    heapq.heapify(nums)
    h = heapq.nlargest(k, nums)
    heapq.heappop(nums)
    return h[-1]


nums = [3, 2, 1, 5, 6, 4]
print(findKthLargest(nums, 2))
"""
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
