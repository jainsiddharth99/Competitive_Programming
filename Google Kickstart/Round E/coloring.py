def coloring(n):
    # base checks
    if n<=5:return 1
    count,bot,john,x=0,1,0,1
    while x<n:
        if count%2==0:
            x+=3
            if x<=n: john+=1
        else:
            x+=2
            if x<=n: bot+=1
        count+=1
    return bot        
    
t=int(input())
res=[]
for i in range(t):
    a=int(input())
    r=coloring(a)
    res.append(r)
    
for i in range(len(res)):
    print('Case #{}:'.format(i+1),res[i] )
