from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, maxx = 0, 0, 0
        cnt = Counter()
        while r < len(s):
            cnt[s[r]] += 1

            if (r-l+1) - max(cnt.values()) <= k:
                maxx = max(maxx, r-l+1)
            else:
                cnt[s[l]] -= 1
                if not cnt[s[l]]:
                    cnt.pop(s[l])
                l += 1

            r += 1
        return len(s)-l


A = Solution()
s = "AABABBA"
k = 1
print(A.characterReplacement(s, k))
