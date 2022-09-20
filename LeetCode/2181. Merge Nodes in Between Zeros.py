# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lt = []
        t = 0
        while head:
            if head.val == 0:
                lt.append(t)
                head = head.next
                t = 0
            else:
                t += head.val
                head = head.next
        curr = dummy = ListNode(lt[0])
        for i in lt[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
