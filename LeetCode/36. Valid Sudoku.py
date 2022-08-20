def isValidSudoku(board):
    row={}
    column={}
    box=[]
    
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box.append(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3])
    l='.'       
    for k in box:
        while l in k:
            
            k.remove(l)          
                
    
    
    for i in range(1,10):
        row[i]={}
        column[i]={}

    for i in range(1,10):
        for j in range(1,10):
            row[i][j]=0
            column[i][j]=0

    
            
    #print (row)
    for i in range(9):
        for j in range(9):
            cur=board[i][j]
            if cur !='.':
                cur=int(cur)
                # for row
                if cur in row[i+1] and row[i+1][cur]==1:
                    return False
                if cur in row[i+1] and row[i+1][cur]==0:
                    row[i+1][cur]+=1
                
                  
                
                # for column
                if cur in column[j+1] and column[j+1][cur]==1:
                    return False
                if cur in column[j+1] and column[j+1][cur]==0:
                    column[j+1][cur]+=1
    count=0
    for i in range(1,10):
        for j in range(1,10):
            if row[i][j]!=0:
                count+=1
    if count==0: return True
                
                
    for m in box:
        if len(m)-len(set(m))!=0:
            return False                         
                        
    return True
                



board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
ans=isValidSudoku(board)
print (ans)