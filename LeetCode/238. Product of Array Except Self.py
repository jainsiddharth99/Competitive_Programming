import numpy as np


def productExceptSelf(nums: list[int]) -> list[int]:
    output = [1]*len(nums)
    n = len(nums)

    prod = 1
    for i in range(1, n):
        prod *= nums[i-1]
        output[i] *= prod

    prod = 1
    for i in range(n-2, -1, -1):
        prod *= nums[i+1]
        output[i] *= prod

    return output

    # approach that did not pass a test case
    # n= len(nums)
    #     res=[1]*n
    #     for i in  range(n):
    #         rest=nums[i+1:] +nums[:i]
    #         res[i]=np.prod(rest)
    #     return res


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))

"""
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
