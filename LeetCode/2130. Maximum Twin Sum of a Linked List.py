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
