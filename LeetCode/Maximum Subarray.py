
def maxv(nums):
    res=0
    current=0
    n=len(nums)
    for i in range(n):
        for j in range(i,n+1):
            if j<n and nums[i]+nums[j]>current :
                val=nums[i]+nums[j]
                current+=val
                
            if j<n and nums[i]+nums[j]<current:
                res=0  
    return res
nums = [-2,1,-3,4,-1,2,1,-5,4]
u=maxv(nums)
print(u)
    
    