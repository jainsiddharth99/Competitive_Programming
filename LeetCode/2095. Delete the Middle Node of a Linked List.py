# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        c = 0
        while fast and fast.next:
            c += 1
            slow = slow.next
            fast = fast.next.next
        if c == 0:
            return None
        curr = head
        while curr:
            if curr.next == slow:
                curr.next = curr.next.next
            curr = curr.next
        return head
