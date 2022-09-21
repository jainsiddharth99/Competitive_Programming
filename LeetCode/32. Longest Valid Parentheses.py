class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        count = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    length = i-stack[-1]
                    count = max(count, length)
        return count


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxc = 0
        l, r = 0, 0
        for i in s:
            if i == '(':
                l += 1
            else:
                r += 1
            if l == r:
                maxc = max(maxc, 2*l)
            elif r > l:
                l, r = 0, 0
        s = s[::-1]
        l, r = 0, 0
        for i in s:
            if i == '(':
                l += 1
            else:
                r += 1
            if l == r:
                maxc = max(maxc, 2*l)
            elif l > r:
                l, r = 0, 0
        return maxc
