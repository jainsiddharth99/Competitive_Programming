from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q=deque([i for i in range(1,n+1)])

        while len(q)>1:
            q.rotate(-k)
            q.pop()
        return q.pop()