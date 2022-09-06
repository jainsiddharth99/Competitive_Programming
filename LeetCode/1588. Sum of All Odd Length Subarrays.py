class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        s = 0
        for i in range(n):
            for j in range(i, n, 2):
                s += sum(arr[i:j+1])

        return s
