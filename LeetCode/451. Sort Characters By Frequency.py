from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        dt = Counter(s)
        cnt = dict(sorted(dt.items(), key=lambda x: x[1], reverse=True))
        res = ""
        for k, v in cnt.items():
            res += k*v
        return res
