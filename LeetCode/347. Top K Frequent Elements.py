from collections import defaultdict


def topKFrequent(nums: list[int], k: int) -> list[int]:
    dt = defaultdict(int)
    for i in nums:
        dt[i] += 1

    x = dict(sorted(dt.items(), key=lambda x: x[1], reverse=True))
    res = []
    for key in x.keys():
        res.append(key)
    return res[:k]


nums = [1, 1, 1, 2, 2, 5, 5, 3]
print(topKFrequent(nums, 2))


"""
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
"""
