class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        i = 0
        j = k
        while j <= len(nums):
            med = self.median(nums[i:j], k)
            res.append(med)
            i += 1
            j += 1
        return res

    def median(self, num, k):
        num.sort()

        if len(num) % 2 == 1:
            return num[k//2]
        else:
            val = num[k//2]+num[(k//2)-1]
            val /= 2
            return val
