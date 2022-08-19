def getConcatenation( nums: list[int]) -> list[int]:
    return nums*2

def solve(A):
    res=[]
    for i in range(len(A)):
        for j in range(len(res)):
            if res[j]==A[i]:
                res[j]+=1
                res.append(A[i])
            else:
                res.append(A[i])
    return res
nums = [1,2]
# ans=getConcatenation(nums)
ans= solve(nums)
print(ans)