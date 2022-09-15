# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow

        prev, next, curr = None, None, mid

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        r_head = prev

        left, right = head, r_head

        while right.next:
            tmp = left.next
            left.next = right
            left = tmp

            tmp = right.next
            right.next = left
            right = tmp
