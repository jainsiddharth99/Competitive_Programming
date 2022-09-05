"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        out = []
        while len(stack):
            temp = stack.pop()
            out.append(temp.val)
            stack.extend(reversed(temp.children))
        return out
