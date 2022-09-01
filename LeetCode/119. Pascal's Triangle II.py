import math


def getRow(rowIndex: int) -> list[int]:
    # n = rowIndex+1
    #     # Edge cases
    # if n == 0:
    #     return []
    # if n == 1:
    #     return [1]
    # if n == 2:
    #     return [1, 1]

    # # 2 initila values
    # res = [[1], [1, 1]]
    # # main logic
    # for i in range(2, n):  # starting with 2 since we dealt with some edge cases
    #     curr = [1]
    #     for j in range(1, i):  # starting
    #         curr.append(res[-1][j-1]+res[-1][j])
    #     curr.append(1)
    #     res.append(curr)
    # return res[-1]

    # 2nd sol

    # edge cases
    r = rowIndex

    if r == 0:
        return [1]
    if r == 1:
        return [1, 1]

    res = [1]
    fact_r = math.factorial(r)
    for i in range(1, r):
        a = (fact_r) // (math.factorial(r-i) * (math.factorial(i)))
        res.append(a)
    res.append(1)
    return res


print(getRow(5))
