class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dt = dict()
        cnt = 0
        maxx = 0
        for i, v in enumerate(nums):
            if v == 0:
                cnt -= 1
            else:
                cnt += 1
            if cnt == 0:
                maxx = i+1
            if cnt in dt:
                maxx = max(maxx, i-dt[cnt])
            else:
                dt[cnt] = i
        return maxx
