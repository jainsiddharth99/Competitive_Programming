
def maxSubArray(nums: list[int]) -> int:
    maxsum=currsum=nums[0]
    
    n= len(nums)
    # base case    
    
    for i in range(1,n):
        # # simple way
        # if currsum+nums[i]>nums[i]:
        #     currsum=currsum+nums[i]
        # else:
        #     currsum=nums[i]
        
        # if currsum>maxsum:
        #     maxsum=currsum
        
        # better way
        currsum=max(currsum+nums[i],nums[i])
        maxsum=max(maxsum,currsum)
    return maxsum

def kadanesalgo(nums: list[int])-> int:
    curr=0
    maxx=float('-inf')
    n=len(nums)
    for i in range(0,n):
        curr=max(nums[i],nums[i]+curr)
        maxx=max(maxx,curr)
    return maxx

def kadanesalgo2(nums: list[int])-> int:
    curr=nums[-1]
    maxx=float('-inf')
    n=len(nums)
    for i in range(n-1,0,-1):
        curr=max(nums[i-1],nums[i-1]+curr)
        maxx=max(maxx,curr)
    return maxx
        
nums = [-2,1,-3,4,-1,2,1,-5,4]
ans=maxSubArray(nums)
ans2=kadanesalgo(nums)
ans3=kadanesalgo2(nums)
print (ans,ans2,ans3)
