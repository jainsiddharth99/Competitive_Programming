def coloring(n):
    lt=[]
    count=0
    for i in range(n):
        lt.append('white')
    l=len(lt)
    
    # base checks
    if l==1 or l==2 or l==3: return 1
    
    if l %2==1:
        lt[0]='red'
        lt[-1]='red'
    else:
        lt[0]='red'
        
    for i in range(1,n-1):
        if lt[i-1]=='white' and lt[i+1]=='white': 
            lt[i]='red'
    
    for i in lt:
        if i=='red':
            count+=1
            
    if count%2==0:
        return count//2
    else:
        return (count//2)+1
    

    
t=int(input())
res=[]
for i in range(t):
    a=int(input())
    r=coloring(a)
    res.append(r)
    
for i in range(len(res)):
    print('Case #{}: '.format(i+1),res[i] )