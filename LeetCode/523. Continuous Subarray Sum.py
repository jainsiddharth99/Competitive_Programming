class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dt = {0: -1}
        summ = 0
        for i, num in enumerate(nums):
            summ += num
            summ %= k
            if summ not in dt:
                dt[summ] = i
            else:
                if i - dt[summ] > 1:
                    return True
        return False
