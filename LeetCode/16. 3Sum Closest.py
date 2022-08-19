def threeSumClosest(nums,target):
    nums.sort()
    currsum=0
    # closestsum=float("inf")
    closestsum=nums[0]+nums[1]+nums[2]
    n=len(nums)
    #* brute force
    # for i in range(0,n):
    #     for j in range(i+1,n):
    #         for k in range(j+1,n):
    #             currsum=nums[i]+nums[j]+nums[k]   
    #             if currsum==target : return target  
    #             if abs(closestsum-target)>abs(currsum-target):
    #                 closestsum=currsum
                    
    #* efficient approach 
    for i in range(0,n-2):
        j=i+1
        k=n-1
        
        while j<k:
            currsum=nums[i]+nums[j]+nums[k]
            diff=abs(currsum-target)
            if abs(closestsum-target)>diff:
                closestsum=currsum
            if target>currsum:
                j+=1
            else:    
                k-=1
    
 
    return closestsum        
    
nums = [-1,2,1,-4]
ans=threeSumClosest(nums,1)
print(ans)