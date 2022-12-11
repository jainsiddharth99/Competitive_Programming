class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        d = {}

        def isi(s1, s2, s3):
            if not (s1 or s2 or s3):
                return True
            if len(s1)+len(s2) != len(s3):
                return False
            if (s1, s2) in d:
                return d[s1, s2]
            val = None
            if '' in (s1, s2):
                val = (s1 or s2)[0] == s3[0] and isi(
                    (s1 or s2)[1:], '', s3[1:])
            elif s3[0] not in (s1[0], s2[0]):
                val = False
            else:
                val = (s1[0] == s3[0] and isi(s1[1:], s2, s3[1:])) or (
                    s2[0] == s3[0] and isi(s1, s2[1:], s3[1:]))
            d[s1, s2] = val
            return val
        return isi(s1, s2, s3)
