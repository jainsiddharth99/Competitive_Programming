# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        val = head
        c = 1
        while val.next:
            c += 1
            val = val.next
        if c == 1:
            return None
        if c == n:
            val = head
            return val.next
        val = head
        c2 = 0
        while val:
            if c2 == c-n-1:
                if not val.next:
                    val.next = None
                    break
                val.next = val.next.next
                break
            c2 += 1
            val = val.next
        return head
