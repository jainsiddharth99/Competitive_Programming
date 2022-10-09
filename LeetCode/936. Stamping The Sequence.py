def movesToStamp(stamp: str, target: str) -> list[int]:

    l_s, l_t = len(stamp), len(target)
    s = '?'*l_t
    res = []

    perm = set()
    for i in range(l_s):
        for j in range(l_s-i):
            perm.add('?'*i + stamp[i:l_s-j] + '?'*j)

    while target != s:
        found = False
        for i in range(l_t-l_s, -1, -1):
            if target[i:i+l_s] in perm:
                target = target[:i]+'?'*l_s+target[i+l_s:]
                res.append(i)
                found = True
        if not found:
            return []

    return res[::-1]


stamp = "abc"
target = "ababc"
print(movesToStamp(stamp, target))

"""
 

Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
Explanation: Initially s = "?????".
- Place stamp at index 0 to get "abc??".
- Place stamp at index 2 to get "ababc".
[1,0,2] would also be accepted as an answer, as well as some other answers.
Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
Explanation: Initially s = "???????".
- Place stamp at index 3 to get "???abca".
- Place stamp at index 0 to get "abcabca".
- Place stamp at index 1 to get "aabcaca".
"""
