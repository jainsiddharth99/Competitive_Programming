def strStr(haystack: str, needle: str) -> int:
    i = 0
    j = len(needle)
    while j <= len(haystack):
        curr = haystack[i:j]
        if curr == needle:
            return i
        i += 1
        j += 1
    return -1


haystack = "leetcode"
needle = "ode"
print(strStr(haystack, needle))
