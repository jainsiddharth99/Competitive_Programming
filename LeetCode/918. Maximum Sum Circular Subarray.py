class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        maxx = minn = curr_min = curr = nums[0]
        total = sum(nums)
        for i in nums[1:]:
            curr = max(i, i+curr)
            maxx = max(maxx, curr)
            curr_min = min(i, i+curr_min)
            minn = min(curr_min, minn)

        return maxx if minn == total else max(maxx, total-minn)
