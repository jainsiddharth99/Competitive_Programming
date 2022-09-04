import numpy as np


def maxProduct(nums: list[int]) -> int:
    # brute force
    # n = len(nums)
    # if n == 1:
    #     return nums[-1]
    # maxP = 0
    # for i in range(n):
    #     for j in range(i, n):
    #         curr = np.prod(nums[i:j+1])
    #         maxP = max(maxP, curr)

    # return maxP
    res = max(nums)
    maxP, minP = 1, 1
    for n in nums:
        if n == 0:
            maxP, minP = 1, 1
            continue
        tmp = maxP*n
        maxP = max(n, maxP*n, minP*n)
        minP = min(n, tmp, minP*n)
        res = max(res, maxP)

    return res


nums = [-3, 0, 1, -2]
print(maxProduct(nums))

"""
Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.


Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
