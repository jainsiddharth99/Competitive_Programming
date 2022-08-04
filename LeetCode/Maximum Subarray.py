
def maxSubArray(nums: list[int]) -> int:
    maxsum=currsum=nums[0]
    
    n= len(nums)
    # base case    
    
    for i in range(1,n):
        if currsum+nums[i]>nums[i]:
            currsum=currsum+nums[i]
        else:
            currsum=nums[i]
        
        if currsum>maxsum:
            maxsum=currsum
        
        
    return maxsum

nums = [-2,1,-3,4,-1,2,1,-5,4]
ans=maxSubArray(nums)
print (ans)
