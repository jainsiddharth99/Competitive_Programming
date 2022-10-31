from collections import Counter


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for k, v in cnt.items():
            if v > 2:
                while v > 2:
                    nums.remove(k)
                    v -= 1
        return len(nums)
