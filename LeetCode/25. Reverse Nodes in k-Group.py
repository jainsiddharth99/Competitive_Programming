class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        itr = ans = ListNode()  # dummy head
        st = []  # define stack
        while head:
            i = k
            while i > 0 and head:  # iterate until a group can be formed
                st.append(head.val)  # push node values to stack
                head = head.next
                i -= 1
            if i != 0:  # if not a full group (has length  < k) then reverse stack since linked list nodes need not be reversed
                st = st[::-1]
            while st:   # pop from stack till empty and form the list in reverse order
                itr.next = ListNode(st.pop())
                itr = itr.next
        return ans.next  # return node after dummy head