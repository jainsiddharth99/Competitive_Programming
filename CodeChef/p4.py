n=int(input())
p=int(input())
lt=[]
for i in range(n):
    a=int(input())
    lt.append(a)
total=0
for i in range(1,100):
    for j in  range(n):
        total+=i//lt[j]
    if p<=total:
        print(i)
        exit()