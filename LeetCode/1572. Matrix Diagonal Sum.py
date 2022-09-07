def diagonalSum(mat: list[list[int]]) -> int:
    res = 0
    n = len(mat)
    # left_diagonal
    for i in range(n):
        res += mat[i][i]
    if n % 2 == 0:
        s, e = 0, n-1
        while s != n:
            res += mat[s][e]
            s += 1
            e -= 1
    else:
        s, e = 0, n-1
        while s != n:
            if s == e:
                s += 1
                e -= 1
                continue
            res += mat[s][e]
            s += 1
            e -= 1
    return res


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
print(diagonalSum(mat))

"""
Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once

Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:

Input: mat = [[5]]
Output: 5
"""
