from collections import defaultdict, Counter


def checkInclusion1(self, s1: str, s2: str) -> bool:
    dt_s1 = defaultdict(int)
    for i in s1:
        dt_s1[i] += 1
    n = len(s1)
    dt_s2 = defaultdict(int)
    for i in s2[:n]:
        dt_s2[i] += 1
    m = len(s2)
    for i in range(m):
        if dt_s1 == dt_s2:
            return True
        j = i+n
        dt_s2[s2[j]] += 1
        dt_s2[s2[i]] -= 1
    return False


def checkInclusion2(s1: str, s2: str) -> bool:
    dt_s1 = Counter(s1)
    n = len(s1)
    dt_s2 = Counter(s2[:n])
    m = len(s2)
    for i in range(m-n+1):
        if dt_s1 == dt_s2:
            return True
        j = i+n
        if j < m:
            dt_s2[s2[j]] += 1
        if dt_s2[s2[i]] > 1:
            dt_s2[s2[i]] -= 1
        else:
            dt_s2.pop(s2[i])
    return False


s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion2(s1, s2))
"""
Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""
