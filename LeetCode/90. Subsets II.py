class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in sorted(nums):
            for j in range(len(res)):
                res += [res[j]+[i]]
        return set(tuple(ele) for ele in res)
