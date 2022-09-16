"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head
        lt = []
        while head:
            if head.child:
                lt.append(head.val)
                lt.extend(self.child(head.child))
                head = head.next
            if head:
                lt.append(head.val)
                head = head.next

        cur = dummy = Node(lt[0], None, None, None)

        for i in range(1, len(lt)):
            cur.next = Node(lt[i], cur, None)
            cur = cur.next
        return dummy

    def child(self, head):
        lt = []
        while head:
            if head.child:
                lt.append(head.val)
                lt.extend(self.child(head.child))
                head = head.next
            if head:
                lt.append(head.val)
                head = head.next
        return lt


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head:
            s = []
            curr = head
            while curr:
                if curr.next:
                    s.append(curr.next)
                if curr.child:
                    s.append(curr.child)
                    curr.child = None
                if s:
                    next = s.pop()
                    curr.next = next
                    next.prev = curr

                curr = curr.next
        return head
