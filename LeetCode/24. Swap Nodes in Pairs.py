# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None and head.next != None:
            head.val, head.next.val = head.next.val, head.val
            self.swapPairs(head.next.next)
        return head


# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         tmp=head
#         if tmp is None:return
#         while tmp and tmp.next:
#             if tmp.val!=tmp.next.val:
#                 tmp.val,tmp.next.val=tmp.next.val,tmp.val
#             tmp=tmp.next.next
#         return head
