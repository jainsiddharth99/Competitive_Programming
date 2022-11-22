from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnt=Counter(nums)
        res=[]
        c=0
        for k,v in cnt.items():
            if v==1:
                c+=1
                res.append(k)
            if c==2:
                break
        return res
