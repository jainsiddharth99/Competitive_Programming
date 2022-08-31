def generate(numRows):
    n = numRows

    if n == 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    res = [[1], [1, 1]]

    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            row.append(res[i-1][j-1]+res[i-1][j])
        row.append(1)
        res.append(row)

    return res


numRows = 5
print(generate(numRows))

"""
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
