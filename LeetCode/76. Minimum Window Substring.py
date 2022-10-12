from collections import defaultdict, Counter


def minWindow(s: str, t: str) -> str:
    # base cases
    if s == t:
        return s
    if len(s) < len(t):
        return ""
    # main
    dt_t = Counter(t)
    dt_s = Counter()

    res = ""
    start = 0
    end = 0
    while end < len(s):
        if s[end] in dt_t.keys():
            dt_s[s[end]] += 1
        while (dt_s & dt_t) == dt_t:
            if len(res) > end-start+1 or not res:
                res = s[start:end+1]
            dt_s[s[start]] -= 1
            start += 1
        end += 1

    return res


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))

"""
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 """
