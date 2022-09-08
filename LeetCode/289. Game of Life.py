def gameOfLife(board: list[list[int]]) -> None:
    row = len(board)
    col = len(board[0])
    to_zero = []
    to_one = []
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, 1],
            [1, 1], [1, 0], [1, -1], [0, -1]]
    for i in range(row):
        for j in range(col):
            count = 0
            for l, r in dirs:
                l += i
                r += j
                if 0 <= l < row and 0 <= r < col and abs(board[l][r]) == 1:
                    count += 1
            if board[i][j] == 1:
                if count < 2:
                    to_zero.append((i, j))
                elif count > 3:
                    to_zero.append((i, j))
            else:
                if count == 3:
                    to_one.append((i, j))

    for i in to_zero:
        a, b = i
        board[a][b] = 0
    for i in to_one:
        a, b = i
        board[a][b] = 1
    print(board)


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
gameOfLife(board)

"""
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
"""
