from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = len(nums)//3
        res = []
        cnt = Counter(nums)
        for k, v in cnt.items():
            if v > c:
                res.append(k)
        return res
