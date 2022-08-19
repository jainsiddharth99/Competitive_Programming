def isValidSudoku(board):
    row={}
    column={}
    box={}
    for i in range(1,10):
        row[i]={}
        column[i]={}
        box[i]={}
    for i in range(1,10):
        for j in range(1,10):
            row[i][j]=None
            column[i][j]=None
            box[i][j]=None

    for i in range(0,9):
        for j in range(0,9):
            column[i+1][j+1]=board[j][i]
    return column



board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

ans=isValidSudoku(board)
print (ans)