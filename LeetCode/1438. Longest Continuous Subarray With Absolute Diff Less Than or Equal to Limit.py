from collections import deque


def longestSubarray(nums: list[int], limit: int) -> int:
    incq = deque()
    decq = deque()
    ans = 0
    s = e = 0
    while e < len(nums):
        curr = nums[e]

        while incq and incq[-1] < curr:
            incq.pop()
        incq.append(curr)

        while decq and decq[-1] > curr:
            decq.pop()
        decq.append(curr)

        while incq[0] - decq[0] > limit:
            if incq[0] == nums[s]:
                incq.popleft()

            if decq[0] == nums[s]:
                decq.popleft()
            s += 1
        ans = max(ans, e-s+1)
        e += 1
    return ans


nums = [10, 1, 2, 4, 7, 2]
print(longestSubarray(nums, 5))

"""
Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
"""
