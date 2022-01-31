accounts = [[1,2,3],[3,2,1]]

print(max(sum(acc) for acc in accounts))

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         t=[]
#         for i in accounts:
#             a=sum(i)
#             t.append(a)
#         return max(t)

# ------------------------or------------------------

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         return max(sum(i) for i in accounts)
        