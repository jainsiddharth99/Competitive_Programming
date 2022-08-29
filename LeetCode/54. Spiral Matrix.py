def spiral(matrix):
    '''
    Edge cases:

    1. As first will be the first elements always we can add
    them initially
    '''
    # res = []
    # m, n = len(matrix), len(matrix[0])
    # a = m*n

    # first_row, first_col = 0, 0
    # while first_row < n and first_col < m:
    #     # First Row

    #     for i in range(first_row, n):
    #         res += [matrix[first_row][i]]
    #     first_row += 1

    #     if len(res) == a:
    #         break

    #     # Last column

    #     for j in range(first_row, m):
    #         res += [matrix[j][n-1]]
    #     if len(res) == a:
    #         break

    #     n -= 1
    #     # last row
    #     for k in range(n-1, first_col, -1):
    #         res += [matrix[m-1][k]]
    #     if len(res) == a:
    #         break

    #     m -= 1
    #     # first col
    #     for l in range(m, first_col, -1):
    #         res += [matrix[l][first_col]]
    #     first_col += 1
    #     if len(res) == a:
    #         break

    # return res

    # 2nt try

    start_row = 0
    start_col = 0
    end_row = len(matrix)-1
    end_col = len(matrix[0])-1
    total = len(matrix)*len(matrix[0])
    count = 0
    res = []

    """
    Matrix = [  [1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15]]
                
                now matrix[0] is our start row
                it start is 0 to end_col== -4
                
                for first col -[1,6,11]
                start is 0 and end is end row->2
    """

    while count < total:

        for i in range(start_row, end_col+1):
            res.append(matrix[start_row][i])
            count += 1
        if count == total:
            break

        start_row += 1

        for i in range(start_row, end_row+1):
            res.append(matrix[i][end_col])
            count += 1
        if count == total:
            break
        end_col -= 1

        for i in range(end_col, start_col-1, -1):
            res.append(matrix[end_row][i])
            count += 1
        if count == total:
            break
        end_row -= 1

        for i in range(end_row, start_row-1, -1):
            res.append(matrix[i][start_col])
            count += 1
        if count == total:
            break
        start_col += 1

    return res


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(spiral(matrix))
