# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while left > 1:
            prev = curr
            curr = curr.next
            left, right = left-1, right-1
        tail, con = curr, prev

        while right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            right -= 1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = curr
        return head
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

#         if right<=left:
#             return head
#         dummy=ListNode(0)
#         dummy.next=head

#         pre = dummy
#         curr=dummy.next

#         for  i in range(1,left):
#             pre=pre.next
#             curr=curr.next

#         for i in range(right-left):
#             tmp=curr.next
#             curr.next=tmp.next
#             tmp.next=pre.next
#             pre.next=tmp
#         return dummy.next
