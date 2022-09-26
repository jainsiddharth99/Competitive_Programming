class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        s = []
        for i in arr:
            curr = i
            while s and s[-1] > i:
                curr = max(curr, s.pop())
            s.append(curr)
        return len(s)
