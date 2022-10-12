from collections import Counter


def longestSubstring(s: str, k: int) -> int:
    if k > len(s):
        return 0
    cnt = Counter(s)

    ans = 0
    i = 0
    flag = False
    for j in range(len(s)):
        if cnt[s[j]] < k:
            ans = max(ans, longestSubstring(s[i:j], k))
            i = j+1
            flag = True
    return max(ans, longestSubstring(s[i:], k)) if flag else len(s)


s = "aaabb"
k = 3
print(longestSubstring(s, k))
"""
Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
