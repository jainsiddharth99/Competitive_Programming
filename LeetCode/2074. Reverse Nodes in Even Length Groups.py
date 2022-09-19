# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        a = []
        while curr:
            a.append(curr.val)
            curr = curr.next
        n = len(a)
        i, k = 0, 1
        while i < n:
            if min(n-i, k) % 2 == 0:
                a[i:i+k] = a[i:i+k][::-1]

            i += k
            k += 1
        curr = head
        for i in a:
            curr.val = i
            curr = curr.next
        return head
