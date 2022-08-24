def rotate(matrix):
    matrix.reverse()
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
