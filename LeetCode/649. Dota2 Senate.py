from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q_r = deque()
        q_d = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'D':
                q_d.append(i)
            else:
                q_r.append(i)

        while q_r and q_d:
            r_index = q_r.popleft()
            d_index = q_d.popleft()
            if r_index < d_index:
                q_r.append(r_index+n)
            else:
                q_d.append(d_index+n)

        return 'Dire' if q_d else 'Radiant'
