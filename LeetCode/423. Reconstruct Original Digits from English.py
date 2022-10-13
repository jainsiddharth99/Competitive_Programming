from collections import Counter


def originalDigits(s: str) -> str:
    cnt = Counter(s)
    res = [0 for i in range(10)]

    # odd count
    res[0] = cnt['z']
    res[2] = cnt['w']
    res[4] = cnt['u']
    res[6] = cnt['x']
    res[8] = cnt['g']

    # even count
    res[1] = cnt['o'] - (res[0]+res[2]+res[4])
    res[3] = cnt['r'] - (res[0] + res[4])
    res[5] = cnt['f'] - res[4]
    res[7] = cnt['s'] - res[6]
    res[9] = cnt['i'] - (res[5]+res[6]+res[8])

    return "".join(str(i)*v for i, v in enumerate(res))


s = "owoztneoer"
print(originalDigits(s))
