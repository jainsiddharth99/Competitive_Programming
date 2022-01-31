accounts = [[1,2,3],[3,2,1]]
l=[]
for i in accounts:
    a=sum(i)
    l.append(a)
print (max(l))

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         t=[]
#         for i in accounts:
#             a=sum(i)
#             t.append(a)
#         return max(t)
        