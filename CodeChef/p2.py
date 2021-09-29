import string
n=input()
n=n.lower()
l1=[]
count=0
dict1=dict(zip(string.ascii_lowercase,range(0,26)))
for i in n:
    l1.append(i)
for i in range(len(l1)):
    if i==dict1[l1[i]]:
        count+=1
print(count)