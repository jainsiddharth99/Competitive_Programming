# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        total = 0
        dic = {0: dummy}
        while head:
            total += head.val
            dic[total] = head
            head = head.next

        head = dummy
        total = 0
        while head:
            total += head.val
            head.next = dic[total].next
            head = head.next

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return []
        lt = []
        c = head
        while c:
            if c.val:
                lt.append(c.val)
            c = c.next
        n = len(lt)
        s = []

        for i in lt:
            if s:
                total = i
                for j in range(len(s)-1, -1, -1):
                    total += s[j]
                    if total == 0:
                        s = s[:j]
                        break
                else:
                    s.append(i)

            else:
                s.append(i)

        curr = dummy = ListNode(0)
        for i in s:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
