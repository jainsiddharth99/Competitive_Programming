# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lt = []
        while head:
            lt.append(head.val)
            head = head.next

        n = len(lt)
        total = float("-inf")
        i = 0
        while i < n-1:
            total = max(total, lt[i]+lt[n-1])
            i += 1
            n -= 1
        return total


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

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

        total = float("-inf")
        while head and r_head:
            total = max(total, head.val+r_head.val)
            head = head.next
            r_head = r_head.next
        return total


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        s = []
        while slow:
            s.append(slow.val)
            slow = slow.next
        total = float("-inf")
        while s:
            total = max(total, head.val+s.pop())
            head = head.next
        return total
