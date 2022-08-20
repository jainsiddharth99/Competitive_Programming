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
            row[i][j]=0
            column[i][j]=0
            box[i][j]=0
            
    #print (row)
    for i in range(9):
        for j in range(9):
            cur=board[i][j]
            if cur !='.':
                cur=int(cur)
                # for row
                if cur in row[i+1] and row[i+1][cur]==0:
                    row[i+1][cur]+=1
                    # for column
                if cur in column[j+1] and column[j+1][cur]==0:
                    column[j+1][cur]+=1
            else:
                pass
                
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