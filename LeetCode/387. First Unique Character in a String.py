from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = Counter(s)
        for i in range(len(s)):
            if res[s[i]] == 1:
                return i
        return -1
