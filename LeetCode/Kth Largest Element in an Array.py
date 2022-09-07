def findKthLargest(nums: list[int], k: int) -> int:
    nums.sort()
    return nums[-k]


"""
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
