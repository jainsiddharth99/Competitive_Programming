# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = head
        c = 0
        while val:
            c += 1
            val = val.next

        if c % 2 == 1:
            c //= 2
        else:
            c /= 2

        val = head
        c2 = 0
        while val:
            if c2 == c:
                return val

            c2 += 1
            val = val.next


# def middleNode(self, head):
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
