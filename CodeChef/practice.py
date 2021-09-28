# n=int(input())
# val=[]
# for i in range(n):
#     v=int(input())
#     val.append(v)
val=[10,5,15,10,20,9,21,21]
ans=[]
for i in range(len(val)):
    print(i)
    if val[i]==val[0] and i==1:
        pass
    elif val[i]==val[-1]:
        pass
    elif val[i+1]>val[i] and val[i-1]>val[i]:
        ans.append(val[i])

print(ans)

