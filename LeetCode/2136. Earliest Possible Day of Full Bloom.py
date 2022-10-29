class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        min_time = float('-inf')
        time = 0
        for grow, curr in reversed(sorted(zip(growTime, plantTime))):
            time += curr
            min_time = max(min_time, time+grow)
        return min_time
