
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        res = [None]*k
        c = 0
        h = head
        while h:
            c += 1
            h = h.next
        part = c//k
        r = c % k  # remainder

        i = 0
        while head is not None:
            c = 1
            if r > 0:
                extra = 1
            else:
                extra = 0

            while c <= part+extra:
                if c == 1:
                    res[i] = head
                if c == part+extra:
                    node = head
                    head = head.next
                    node.next = None
                if c != part+extra:
                    head = head.next
                c += 1
            i += 1
            if r:
                r -= 1
        return res
