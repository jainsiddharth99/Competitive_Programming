class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cp = []
        c = 2
        prev = head
        curr = head.next
        while curr.next:
            if prev.val > curr.val and curr.val < curr.next.val:
                cp.append(c)
            if prev.val < curr.val and curr.val > curr.next.val:
                cp.append(c)
            c += 1
            prev = curr
            curr = curr.next
        n = len(cp)
        if n < 2:
            return [-1, -1]
        elif n == 2:
            return [cp[1]-cp[0], cp[1]-cp[0]]
        else:
            maxd = cp[-1]-cp[0]
            mind = float("inf")
            for i in range(0, n-1):
                j = i+1
                mind = min(mind, cp[j]-cp[i])
            return [mind, maxd]
