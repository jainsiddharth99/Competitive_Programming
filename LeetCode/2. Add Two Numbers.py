
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode(0)
        l = []
        r = []
        while l1:
            l.append(l1.val)
            l1 = l1.next
        while l2:
            r.append(l2.val)
            l2 = l2.next

        s = [str(i) for i in l[::-1]]
        s1 = [str(i) for i in r[::-1]]
        j1 = int("".join(s))
        j2 = int("".join(s1))

        j = j1+j2
        lt = [int(i) for i in str(j)]

        for i in lt[::-1]:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next
