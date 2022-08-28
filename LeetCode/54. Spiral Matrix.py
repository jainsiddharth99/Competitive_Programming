def spiral(matrix):
    '''
    Edge cases:

    1. As first will be the first elements always we can add
    them initially
    '''
    res = []
    m, n = len(matrix), len(matrix[0])
    a = m*n
    if m == 1:
        return matrix[0]

    first_row, first_col = 0, 0
    while first_row < n and first_col < m:
        # First Row

        for i in range(first_row, n):
            res += [matrix[first_row][i]]
        first_row += 1

        if len(res) == a:
            break

        # Last column

        for j in range(first_row, m):
            res += [matrix[j][n-1]]
        if len(res) == a:
            break

        n -= 1
        # last row
        for k in range(n-1, first_col, -1):
            res += [matrix[m-1][k]]
        if len(res) == a:
            break

        m -= 1
        # first col
        for l in range(m, first_col, -1):
            res += [matrix[l][first_col]]
        first_col += 1
        if len(res) == a:
            break

    return res


matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
print(spiral(matrix))
