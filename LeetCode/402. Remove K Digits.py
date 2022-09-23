def removeKdigits(num: str, k: int) -> str:
    n = len(num)
    if n == k:
        return '0'
    s = []
    for i in range(n):
        while s and s[-1] > num[i] and k > 0:
            s.pop()
            k -= 1

        s.append(num[i])
    while k > 0 and s:
        s.pop()
        k -= 1

    if not s:
        return '0'

    if s[0] == '0':
        while s and s[0] == '0':
            s.pop(0)
        if not s:
            return '0'

        return ''.join(s)
    else:
        return ''.join(s)


num = "10200"
k = 3
print(removeKdigits(num, k))
"""
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""
