class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # * edge cases
        if n == 0:
            return []
        if n == 1:
            return [nums]
        res = []
        # * main logic
        for i in range(n):
            fixed = nums[i]
            restlist = nums[:i]+nums[i+1:]
            for i in self.permuteUnique(restlist):
                curr = [fixed]+i
                if curr not in res:
                    res.append(curr)
        return res
