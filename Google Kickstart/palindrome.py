from itertools import combinations

def palindrome(n,p):
    lt,lt1=[],[]
    for i,j in combinations(range(n+1),r=2):
        lt.append(p[i:j])
        
    for i in lt:
        new=p+i
        if new==new[::-1] and i==i[::-1]: lt1.append(i)
    
    lt1.sort(key=len)

    return lt1[0]

t=int(input())
res=[]
for i in range(t):
    N=int(input())
    P=input()
    r=palindrome(N,P)
    print('Case #{}:'.format(i+1),r )
    

    