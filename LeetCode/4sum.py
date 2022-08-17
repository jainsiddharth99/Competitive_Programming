def foursum(nums,target):
    nums.sort()
    n=len(nums)
    res=set()
    #* brute force
    # for i in range(0,n-3):
    #     for j in range(i,n-2):
    #         for k in range(j,n-1):
    #             for l in range(k,n):
    #                 if nums[i]+ nums[j]+nums[k]+ nums[l]==target:
    #                     if ([nums[i],nums[j],nums[k],nums[l]]) not in res and i!=j and j!=k and k!=l:
    #                         res.append([nums[i],nums[j],nums[k],nums[l]])
    
    
    #* efficient approach
    for i in range(0,n-3):
        for j in range(i+1,n-2):
            k=j+1
            l=n-1
            
            while k<l:
                summ=nums[i]+ nums[j]+nums[k]+ nums[l]
                # if nums[i]+ nums[j]+nums[k]+ nums[l]==target:
                #     if ([nums[i],nums[j],nums[k],nums[l]]) not in res and i!=j and j!=k and k!=l:
                #         res.append([nums[i],nums[j],nums[k],nums[l]])
                if summ==target:
                    
                    res.add(tuple([nums[i],nums[j],nums[k],nums[l]]))
                
                if target>summ:
                    k+=1
                else:
                    l-=1
                
    return res

nums = [1,0,-1,0,-2,2]
target=0
ans=foursum(nums,target)
print(ans)