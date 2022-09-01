def subsets(nums):
    res = [[]]
    for i in nums:
        for j in range(len(res)):
            res += [res[j]+[i]]
    return res


nums = [1, 2, 2]
print(subsets(nums))


"""
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
