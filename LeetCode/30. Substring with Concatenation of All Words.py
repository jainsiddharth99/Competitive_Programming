from itertools import permutations
from collections import defaultdict


def findSubstring1(s: str, words: list[str]) -> list[int]:
    p = permutations(words)
    perm = []
    for i, v in enumerate(p):
        perm.append("".join(v))

    res = []
    n = len(perm[0])

    l = 0
    r = n-1
    l_s = len(s)
    while r < l_s:
        curr = s[l:r+1]
        if curr in perm:
            res.append(l)
        l += 1
        r += 1
    return res


def findSubstring2(s: str, words: list[str]) -> list[int]:
    p = permutations(words)
    perm = []
    for i, v in enumerate(p):
        perm.append("".join(v))

    res = []
    n = len(perm[0])

    l = 0
    r = n-1
    l_s = len(s)
    while r < l_s:
        curr = s[l:r+1]
        if curr in perm:
            res.append(l)
            l += len(words[0])-1
            r += len(words[0])-1
        l += 1
        r += 1
    return res


def findSubstring3(s: str, words: list[str]) -> list[int]:
    dt = defaultdict(int)
    for i in words:
        dt[i] += 1
    m, n, l_s = len(words), len(words[0]), len(s)
    i = 0
    j = m*n-1
    res = []
    while j < l_s:
        l = i
        r = i+n-1
        tmp = defaultdict(int)
        while r <= j:
            curr = s[l:r+1]
            tmp[curr] += 1

            l = r+1
            r += n
        if tmp == dt:
            res.append(i)

        i += 1
        j += 1
    return res


s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring3(s, words))

"""

"""
