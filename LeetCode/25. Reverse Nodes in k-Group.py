# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         itr = ans = ListNode()  # dummy head
#         st = []  # define stack
#         while head:
#             i = k
#             while i > 0 and head:  # iterate until a group can be formed
#                 st.append(head.val)  # push node values to stack
#                 head = head.next
#                 i -= 1
#             if i != 0:  # if not a full group (has length  < k) then reverse stack since linked list nodes need not be reversed
#                 st = st[::-1]
#             while st:   # pop from stack till empty and form the list in reverse order
#                 itr.next = ListNode(st.pop())
#                 itr = itr.next
#         return ans.next  # return node after dummy head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k < 2:
            return head

        val = head
        for i in range(k-1):
            val = val.next
            if val is None:
                return head

        prev, curr, nxt = None, head, None

        for i in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head.next = self.reverseKGroup(curr, k)

        return val
