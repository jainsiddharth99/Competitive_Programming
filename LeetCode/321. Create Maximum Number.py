def maxNumber(nums1: list[int], nums2: list[int], k: int) -> list[int]:
    def findmax(nums, length):
        l = []
        maxpop = len(nums)-length
        for i in range(len(nums)):
            while maxpop and l and nums[i] > l[-1]:
                l.pop()
                maxpop -= 1
            l.append(nums[i])
        return l[:length]

    def merge(n1, n2):
        res = []
        while n1 or n2:
            if n1 > n2:
                res.append(n1[0])
                n1 = n1[1:]
            else:
                res.append(n2[0])
                n2 = n2[1:]
        return res

    n1 = len(list(nums1))
    n2 = len(list(nums2))
    res = [0]*k
    for i in range(k+1):
        j = k-i
        if i > n1 or j > n2:
            continue
        l1 = findmax(nums1, i)
        l2 = findmax(nums2, j)
        res = max(res, merge(l1, l2))
    return res


nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
print(maxNumber(nums1, nums2, k))

"""
Example 1:

Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
Output: [9,8,6,5,3]
Example 2:

Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
Output: [6,7,6,0,4]
Example 3:

Input: nums1 = [3,9], nums2 = [8,9], k = 3
Output: [9,8,9]
"""
