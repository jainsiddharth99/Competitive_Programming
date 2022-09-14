# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        prev = dummy = ListNode(0)
        prev.next = head
        while prev:
            if prev.next and prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
