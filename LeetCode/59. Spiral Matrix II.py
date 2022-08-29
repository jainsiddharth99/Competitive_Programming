import numpy as np


def generatematrix(n):
    matrix = np.zeros([n, n], dtype=int)

    total = n*n
    count = 1
    start_row, start_col, end_row, end_col = 0, 0, n-1, n-1
    while count <= total:
        for i in range(start_row, end_col+1):
            matrix[start_row][i] = count
            count += 1
        start_row += 1

        for i in range(start_row, end_row+1):
            matrix[i][end_col] = count
            count += 1

        end_col -= 1

        for i in range(end_col, start_col-1, -1):
            matrix[end_row][i] = count
            count += 1
        end_row -= 1

        for i in range(end_row, start_row-1, -1):
            matrix[i][start_col] = count
            count += 1
        start_col += 1

    return [i for i in matrix]


print(generatematrix(4))
