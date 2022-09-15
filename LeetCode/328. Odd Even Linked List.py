# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = even_l = ListNode(0)
        odd = odd_l = ListNode(0)
        curr = head
        c = 1
        while curr:
            if c % 2 == 1:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            c += 1
            curr = curr.next

        even.next = None
        odd.next = even_l.next
        return odd_l.next
