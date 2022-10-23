from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        dt = Counter(nums)
        for k, v in dt.items():
            if v > 1:
                res.append(k)
                break
        for i in range(1, n):
            if dt[i]:
                continue
            else:
                res.append(i)
        if len(res) == 1:
            res.append(max(nums)+1)
        return res
