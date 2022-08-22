def isValidSudoku(board):
    #* old solution
    # row={}
    # column={}
    # box=[]
    
    
    # for i in range(0, 9, 3):
    #     for j in range(0, 9, 3):
    #         box.append(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3])
    # l='.'       
    # for k in box:
    #     while l in k:
            
    #         k.remove(l)          
                
    
    
    # for i in range(1,10):
    #     row[i]={}
    #     column[i]={}

    # for i in range(1,10):
    #     for j in range(1,10):
    #         row[i][j]=0
    #         column[i][j]=0

    
            
    # #print (row)
    # for i in range(9):
    #     for j in range(9):
    #         cur=board[i][j]
    #         if cur !='.':
    #             cur=int(cur)
    #             # for row
    #             if cur in row[i+1] and row[i+1][cur]==1:
    #                 return False
    #             if cur in row[i+1] and row[i+1][cur]==0:
    #                 row[i+1][cur]+=1
                
                  
                
    #             # for column
    #             if cur in column[j+1] and column[j+1][cur]==1:
    #                 return False
    #             if cur in column[j+1] and column[j+1][cur]==0:
    #                 column[j+1][cur]+=1
    # count=0
    # for i in range(1,10):
    #     for j in range(1,10):
    #         if row[i][j]!=0:
    #             count+=1
    # if count==0: return True
                
                
    # for m in box:
    #     if len(m)-len(set(m))!=0:
    #         return False                         
                        
    # return True
                

    rows=[]
    #* Checking row
    # as board is list of lists
    for i in range(9):
        rows.append(board[i][0:9])
    for row in rows:
        while '.' in row:
            row.remove('.')

        if len(row)!=len(set(row)):
            return False
    #* checking columns
    # since a transpose of matrix can work here
    
    columns = [[board[j][i] for j in range(9)] for i in range(9)]
    for column in columns:
        while '.' in column:
            column.remove('.')
        
        if len(column)!=len(set(column)):
            return False
        
    #* checking 3X3 grids
    # using a list to store 3x3 grid
    
    grids=[]
    for i in range(0,9,3):
        for j in range(0,9,3):
            grids.append(board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3])
    for grid in grids:
        while '.' in grid:
            grid.remove('.')
        
        if len(grid)!=len(set(grid)):
            return False

    return True
            
            


board = [["5","3",".",".","7",".",".",".","."]
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