
def maxSubArray(nums: list[int]) -> int:
    currsum=nums[0]
    n= len(nums)
    # base case     
    # return num[0] if len(nums)==1
    if len(nums)==1 : return nums[0]
    
    for i in range(n):
        for j in range(i,n):
            if sum(nums[i:j+1]) > currsum:
                currsum = sum(nums[i:j+1])
                print(currsum ,'val', nums[i],nums[j])
    return currsum

nums = [-2,1]
ans=maxSubArray(nums)
print (ans)
