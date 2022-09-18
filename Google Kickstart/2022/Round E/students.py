def students(n,lt):
    lt.sort()
    res=[]
    for i in range(n):
        a=i*2
        if a<=lt[i+1]: res.append(lt[i+1])
        
    
t=int(input())
for i in range(t):
    N=int(input())
    lt=[]
    for i in range(N):
        i=int(input()).split()
        lt.append(i)
    r=students(N,lt)
    print('Case #{}:'.format(i+1),r )
    