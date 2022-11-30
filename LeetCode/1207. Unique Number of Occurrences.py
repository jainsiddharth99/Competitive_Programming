from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        res = []
        for k, v in cnt.items():
            res.append(v)
        return len(res) == len(set(res))
