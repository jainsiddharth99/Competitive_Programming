nums = [1,2,3,4]
l=[]
temp=True
for i in nums:
    if i not in l:
        l.append(i)
        temp=False
    else:
        temp=True
print(temp)