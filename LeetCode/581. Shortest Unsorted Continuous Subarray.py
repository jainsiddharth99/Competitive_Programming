def findUnsortedSubarray(nums: list[int]) -> int:
    n = len(nums)
    s = []
    l = float('inf')
    r = float('-inf')

    for i in range(n):
        while s and nums[s[-1]] > nums[i]:
            l = min(l, s.pop())
        s.append(i)
    s = []
    for i in range(n-1, -1, -1):
        while s and nums[i] > nums[s[-1]]:
            r = max(r, s.pop())
        s.append(i)
    return r-l + 1 if r-l > 0 else 0


nums = [2, 6, 4, 8, 10, 9, 15]
print(findUnsortedSubarray(nums))
"""
Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
"""
