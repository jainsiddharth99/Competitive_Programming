from itertools import permutations


def reorderedPowerOf2(n: int) -> bool:

    res = []
    n = str(n)
    for i in range(31):
        res.append(str(pow(2, i)))
    l = []
    for i in permutations(str(n)):
        l.append("".join(i))

    for i in l:
        if i in res and i[0] != 0:
            return True

    return False


print(reorderedPowerOf2(1))
