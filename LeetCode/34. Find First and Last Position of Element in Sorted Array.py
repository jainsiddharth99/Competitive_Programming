def searchRange(nums,target):
    n=len(nums) 
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if nums[start]==nums[end]==target:
            return [start,end]
        else:
            if nums[mid]>target:
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
            else:
                if nums[start]!=target: start+=1
                if nums[end]!=target: end-=1
    
    return [-1,-1]
    
    
    
nums = [5,7,7,8,8,10]
target = 8
ans=searchRange(nums,target)
print(ans) 