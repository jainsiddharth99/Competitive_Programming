class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lt = []
        c = head
        while c:
            lt.append(c.val)
            c = c.next
        n = len(lt)
        s = [lt[0]]

        for i in range(1, n):
            if s[-1]+lt[i] == 0:
                s.pop()
            else:
                s.append(lt[i])
        curr = dummy = ListNode(0)
        for i in s:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
