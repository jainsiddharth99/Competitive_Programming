class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dt = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in dt:
                stack.append(i)
            else:
                if not stack or dt[stack.pop()] != i:
                    return False
        return len(stack) == 0
