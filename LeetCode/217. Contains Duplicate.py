nums = [0,4,5,0,3,6]
l=[]
temp=True
for i in nums:
    if i not in l:
        l.append(i)
        temp=False
    else:
        temp=True
print(temp)

# class Solution(object):
#     def containsDuplicate(self, nums):
#         return True if len(nums) > len(set(nums)) else False