def search(nums,target):
    n=len(nums)
    start=0
    end=n-1
    if nums[start]==target: return start
    if nums[end]==target: return end
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==target:
            return mid
        else:
            if nums[mid]>=nums[start]:                
                if nums[mid]>=target>=nums[start]: 
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[end]>=target>=nums[mid]: 
                    start=mid+1
                else:
                    end=mid-1
    return -1
nums = [5,1,2,3,4]

ans= search(nums,1)
print(ans)