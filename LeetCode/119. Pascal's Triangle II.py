class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        n = rowIndex+1
        # Edge cases
        if n == 0:
            return []
        if n == 1:
            return [1]
        if n == 2:
            return [1, 1]

        # 2 initila values
        res = [[1], [1, 1]]
        # main logic
        for i in range(2, n):  # starting with 2 since we dealt with some edge cases
            curr = [1]
            for j in range(1, i):  # starting
                curr.append(res[-1][j-1]+res[-1][j])
            curr.append(1)
            res.append(curr)
        return res[-1]
