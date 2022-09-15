# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lt = []
        while head:
            lt.append(head.val)
            head = head.next
        lt.sort()

        curr = dummy = ListNode(0)
        for i in lt:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
