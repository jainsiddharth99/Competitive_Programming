def findDuplicate(nums: list[int]) -> int:
    # brute force
    # res=[]
    # for i in nums:
    #     if i in res:
    #         return i
    #     else:
    #         res.append(i)

    # efficient - passes testcases

    # nums.sort()
    # n = len(nums)
    # res = [nums[0]]
    # for i in range(1, n):
    #     if nums[i] == res[-1]:
    #         return nums[i]
    #     else:
    #         res.append(nums[i])

    # simple sol using set
    res = set()
    for i in nums:
        if i in res:
            return i
        res.add(i)


nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))

"""
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
"""
