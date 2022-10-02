class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []
        for i, n in enumerate(nums):
            while s and s[-1] > n and (len(s)-1) + (len(nums)-i) >= k:
                s.pop()
            if len(s) < k:
                s.append(n)
        return s
