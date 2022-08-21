def plusone(digits):
    s=[str(i) for i in digits]
    res=int("".join(s))
    res+=1
    res=str(res)
    s=[int(i) for i in res]
    return s
digits=[1,2,3]
ans=plusone(digits)
print(ans)