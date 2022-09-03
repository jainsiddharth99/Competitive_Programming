from tkinter import N


def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    num = sorted(set(nums))
    n = len(num)
    long = 0
    count = 0
    for i in range(1, n):
        if num[i-1] + 1 == num[i]:
            count += 1
        else:
            long = max(long, count+1)
            count = 0
    long = max(long, count+1)
    return long


nums = [1, 2, 0, 1]
print(longestConsecutive(nums))
"""
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
