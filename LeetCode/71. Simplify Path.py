class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        path = path.split('/')
        for i in path:
            if i == '..':
                if s:
                    s.pop()

            elif i and i != '.':
                s.append(i)

        return '/'+'/'.join(s)
