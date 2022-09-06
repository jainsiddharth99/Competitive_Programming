# O(n)
def findPeakElement(nums: list[int]) -> int:
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i
    return len(nums)-1
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         return search(nums,0,len(nums)-1)


# def search(nums,start,end):
#     if start==end:
#         return start
#     mid=(start+end)//2
#     if nums[mid]<nums[mid+1]:
#         return search(nums,mid+1,end)
#     return search(nums,start,mid)
