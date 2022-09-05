def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    # brue force
    # dt = {n: i for i, n in enumerate(nums1)}
    # n = len(nums1)
    # res = [-1]*n

    # for i in range(len(nums2)):
    #     if nums2[i] not in dt:
    #         continue
    #     else:
    #         for j in range(i+1, len(nums2)):
    #             if nums2[j] > nums2[i]:
    #                 idx = dt[nums2[i]]
    #                 res[idx] = nums2[j]
    #                 break
    # return res

    dt = {n: i for i, n in enumerate(nums1)}
    n = len(nums1)
    res = [-1]*n
    s = []
    for i in range(len(nums2)):
        cur = nums2[i]
        while s and cur > s[-1]:
            val = s.pop()
            idx = dt[val]
            res[idx] = cur
        if cur in nums1:
            s.append(cur)
    return res


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))
"""
Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""
