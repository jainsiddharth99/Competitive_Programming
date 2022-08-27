def spiral(matrx):
    '''
    Edge cases:

    1. As first will be the first elements always we can add
    them initially
    '''
    res = []
    m, n = len(matrix), len(matrix[0])
    if n % 2 == 0:
        ran = n//2
    else:
        ran = (n//2)+1
    # first_row,last_row,first_col,last_col=matrix[0],matrix[-1],

    first_row, first_col, last_row, last_col = 0, 0, m-1, n-1
    i, j = 0, 0
    while ran > 0:
        # first row
        for i in range(first_row, last_col):
            res += [matrix[first_row][i]]
            first_row += 1

        # last col
        for j in range(first_row, last_row):
            res += [matrix[j][last_col]]
            last_col -= 1
        # last row

        for k in range(last_col, first_col, -1):
            res += [matrix[last][k]]

    # for i in matrix[0]:
    #     res += [i]
    # for i in range(1, m):
    #     res += [matrix[i][-1]]
    # for i in range(m-2, -1, -1):
    #     res += [matrix[-1][i]]
    # for i in range(n-2, 0, -1):
    #     res += [matrix[i][0]]

    return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiral(matrix))
