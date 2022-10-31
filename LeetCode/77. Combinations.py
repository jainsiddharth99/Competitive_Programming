from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lt = [i for i in range(1, n+1)]
        return combinations(lt, k)
