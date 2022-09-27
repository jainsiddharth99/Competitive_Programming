def decodeAtIndex(s: str, k: int) -> str:
    res = 0
    for i in s:
        if i.isdigit():
            res *= int(i)
        else:
            res += 1

    for i in reversed(s):
        k %= res
        if k == 0 and i.isalpha():
            return i
        if i.isdigit():
            res /= int(i)
        else:
            res -= 1


s = "leet2code3"
k = 10
print(decodeAtIndex(s, k))
