# brute force
def convert(s,numRows):
    if numRows==1:
        return s
    row=0
    ans=[[]for i in range(numRows)]
    carry=-1
    
    for j in s:
        ans[row].append(j)
        if row==0 or row==numRows-1:
            carry *=-1
        row += carry
    for i in range(len(ans)):
        ans[i]=''.join(ans[i])
    return ''.join(ans)

# second method
# def convert(s,numRows):
#     if numRows==1:
#         return s
#     gap =2*numRows-2
#     ans=[]
#     for i in range(numRows):
#         for j in range(i,len(s),gap):
#             ans.append(s[j])
#             print(ans)
#             step=gap-2*i
#             k = step+j
#             if i!=0 and i!=numRows-1 and k<len(s):
#                 ans.append(s[k])
                
#     return ''.join(ans)

s='paypalishiring'
print(convert(s,3))