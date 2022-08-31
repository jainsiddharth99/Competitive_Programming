from collections import defaultdict


def setzeros(matrix):
    m = len(matrix)
    n = len(matrix[0])
    set_row = set()
    set_col = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                set_row.add(i)
                set_col.add(j)

    for i in range(m):
        for j in range(n):
            if i in set_row or j in set_col:
                matrix[i][j] = 0

    return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(setzeros(matrix))
"""
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
