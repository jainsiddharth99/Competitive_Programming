class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float('inf')
        left=0
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            while summ>=target:
                ans=min(ans,i+1-left)
                summ-=nums[left]
                left+=1
        return ans if ans!=inf else 0
