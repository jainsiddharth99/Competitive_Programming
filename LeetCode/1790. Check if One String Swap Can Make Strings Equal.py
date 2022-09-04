class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        b = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                b.append(i)
        if len(b) > 2:
            return False
        else:
            return sorted(s1) == sorted(s2)
