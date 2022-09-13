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


# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(None, head)
#         prev, val = dummy, head
#         while val and val.next:
#             prev.next = val.next
#             val.next = val.next.next
#             prev.next.next = val
#             prev, val = val, val.next
#         return dummy.next
