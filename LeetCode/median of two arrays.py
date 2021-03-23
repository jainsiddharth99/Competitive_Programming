def findMedianSortedArrays(nums1, nums2):
    nums3=nums1+nums2
    nums3.sort()
    current_node=0
    next_node=0
    if len(nums3)%2==0:
        current_node=len(nums3)//2
        next_node=current_node-1
        median=(nums3[current_node]+nums3[next_node])/2
        # print(median)
    else:
        median=len(nums3)//2
        median=nums3[median]  
    return median   
# if __name__=="__main__":
nums1=[1,2]
nums2=[3,4]
print(findMedianSortedArrays(nums1,nums2))

