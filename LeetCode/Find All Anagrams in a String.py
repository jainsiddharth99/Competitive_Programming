s = "cbaebabacd"
p = "abc"
l=[]
t=""
i=0

while len(p)>=len(t)+1 and i<=len(s)-1:
    t+=s[i]
    i+=1
    
    if len(t)==len(p):
        print(t)
        if sorted(p)==sorted(t):
            l.append(i-len(p))
            t=""
            i=i-len(p)+1
            print(t)
        else:
            t=""
            i=i-len(p)+1
print(t)
print(l)    
    