# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        c = 0
        lt = list1
        while list1:
            if c == a-1:
                prev = list1
            if c == b+1:

                next = list1
            c += 1
            list1 = list1.next

        first = list2
        curr = list2
        while curr.next:
            curr = curr.next
        prev.next = first
        curr.next = next

        return lt
