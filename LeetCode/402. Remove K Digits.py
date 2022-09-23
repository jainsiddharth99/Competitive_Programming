def removeKdigits(num: str, k: int) -> str:
    n = len(num)
    if n == k:
        return '0'
    s = []
    for i in num:
        while s and s[-1] > i and k > 0:
            s.pop()
            k -= 1
        s.append(i)

    if k > 0:
        while k > 0 and s:
            s.pop()
            k = -1
    if not s:
        return '0'

    if s[0] == '0':
        while s and s[0] == '0':
            s.pop(0)
        return "".join(s) if s else '0'
    else:
        return ''.join(s)


num = "1111111"
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
