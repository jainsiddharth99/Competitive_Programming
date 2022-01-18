
roman={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s=input()
ans=0
for i in range(0,len(s)-1):
    if roman[s[i]]<roman[s[i+1]]:
        ans-=roman[s[i]]
    else:
        ans+=roman[s[i]]
        
ans+=roman[s[-1]]
print(ans)
        

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

#         ans=0
#         for i in range(0,len(s)-1):
#             if roman[s[i]]<roman[s[i+1]]:
#                 ans-=roman[s[i]]
#             else:
#                 ans+=roman[s[i]]

#         ans+=roman[s[-1]]
#         return ans
    
    

            