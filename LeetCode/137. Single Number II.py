from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        for k,v in cnt.items():
            if v==1:
                return k
