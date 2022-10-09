from collections import deque


def minKBitFlips(nums: list[int], k: int) -> int:
    n = len(nums)
    cur = res = 0
    for i in range(n):
        if i >= k and nums[i-k] == 2:
            cur -= 1
        if cur % 2 == nums[i]:
            if i+k > n:
                return -1
            nums[i] = 2
            cur += 1
            res += 1
    return res


def minKBitFlips2(nums: list[int], k: int) -> int:
    q = deque()
    ans = 0
    n = len(nums)
    for i in range(n):
        if q and q[0] < i:
            q.popleft()
        if len(q) % 2 == nums[i]:
            if i+k > n:
                return -1
            ans += 1
            q.append(i+k-1)
    return ans


nums = [0, 1, 0]
k = 1
print(minKBitFlips2(nums, k))
"""
Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].
Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
 """
