# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        val = head
        if k == 0:
            return head
        c = 1
        while val.next:
            c += 1
            val = val.next
        print(c)
        if c == 1:
            return head
        k = k % c
        val.next = head

        tmp = head
        for i in range(c-k-1):
            tmp = tmp.next

        ans = tmp.next
        tmp.next = None
        return ans
