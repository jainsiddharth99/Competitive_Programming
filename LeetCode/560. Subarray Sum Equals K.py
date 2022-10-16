from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dt = defaultdict(int)
        dt[0] = 1
        c = pre = 0
        for i in nums:
            pre += i
            if pre-k in dt:
                c += dt[pre-k]
            dt[pre] += 1
        return c
