# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        s = [0]
        res = []
        prev, next = None, None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        head = prev

        while head:
            curr = head.val
            while s[-1] != 0 and s[-1] <= curr:
                s.pop()
            res.append(s[-1])
            s.append(curr)

            head = head.next
        return res[::-1]
