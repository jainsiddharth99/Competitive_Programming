from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)

        cnt = Counter()
        i = 0
        j = 9
        while j < n:
            cnt[s[i:j+1]] += 1
            i += 1
            j += 1
        res = []
        for k, v in cnt.items():
            if v > 1:
                res.append(k)
        return res
