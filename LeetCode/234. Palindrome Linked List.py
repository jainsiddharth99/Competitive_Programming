# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         slow = fast = head 
#         while fast != None and fast.next != None:
#             slow = slow.next 
#             fast = fast.next.next
#         if fast != None:  # case number of elements is odd, move mid to next element.
#             slow = slow.next
        
#         def reverse(head):
#             ans = None
#             while head != None:
#                 next = head.next
#                 head.next = ans
#                 ans = head
#                 head = next
#             return ans
        
#         head2 = reverse(slow) # slow is our mid
#         while head2 != None:
#             if head.val != head2.val:
#                 return False
#             head = head.next
#             head2 = head2.next
#         return True
        

def isPalindrome(x):
    x=str(x)
    print(x)
    x=x.replace(',','')
    print(x)
    x=x.replace(' ','')
    print(x[1:-1])
    print(x[-2:0:-1])
    return (bool(x[1:-1]==x[-2:0:-1]))

x=[1,2,2,1]
if isPalindrome(x):
    print ('true')
else:
    print ('false')
