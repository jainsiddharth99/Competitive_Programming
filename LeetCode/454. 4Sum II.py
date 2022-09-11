from collections import defaultdict


def fourSumCount(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    res = 0
    dt = defaultdict(int)
    for i in nums1:
        for j in nums2:
            dt[i+j] += 1
    for k in nums3:
        for l in nums4:
            res += dt[-(k+l)]

    return res


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]

print(fourSumCount(nums1, nums2, nums3, nums4))
"""
Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0



Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
"""
