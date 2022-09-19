# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        cur = dummy = ListNode(0, head)
        c = 0

        cur = cur.next
        while cur:
            c += 1
            cur = cur.next

        endk = c-k+1
        c = 1
        cur = dummy

        while cur:
            if c == k:
                prestart = cur
            if c == k+1:
                start = cur
            if c == endk:
                preend = cur
            if c == endk+1:
                end = cur
            cur = cur.next
            c += 1
        if start == end:
            return head

        prestart.next, preend.next = end, start
        start.next, end.next = end.next, start.next

        return dummy.next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        c = 0
        while cur:
            c += 1
            cur = cur.next

        endk = c-k+1
        c = 1
        cur = head
        while cur:
            if c == k:
                start = cur
            if c == endk:
                end = cur
            c += 1
            cur = cur.next

        start.val, end.val = end.val, start.val
        return head
