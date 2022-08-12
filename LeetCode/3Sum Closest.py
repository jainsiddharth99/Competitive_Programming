def threeSumClosest(nums,target):
    currsum=0
    closestsum=float("inf")
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                currsum=nums[i]+nums[j]+nums[k]
                closestsum=min(abs(closestsum-target),abs(currsum-target))
                closestsum=closestsum+target
    return closestsum        

nums = [-1,2,1,-4]
ans=threeSumClosest(nums,1)
print(ans)