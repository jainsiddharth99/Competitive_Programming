n=int(input())
m=int(input())
nlist=[]
mlist=[]
count=0
for i in range(n):
    a=int(input())
    nlist.append(a)
for j in range(m):
    b=int(input())
    mlist.append(b)
for i in nlist:
    for j in mlist:
        c=i*j
        if c%2==0:
            count+=1
            
            
print(count)