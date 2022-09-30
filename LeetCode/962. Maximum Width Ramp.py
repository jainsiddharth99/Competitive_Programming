def maxWidthRamp(nums: list[int]) -> int:
    res = 0
    s = []
    for i, v in enumerate(nums):
        if not s or nums[s[-1]] > v:
            s.append(i)
    for j in range(len(nums)-1, -1, -1):
        while s and nums[s[-1]] <= nums[j]:
            res = max(res, j-s.pop())

    return res


nums = [6, 0, 8, 2, 1, 5]
print(maxWidthRamp(nums))


"""
Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 
"""
