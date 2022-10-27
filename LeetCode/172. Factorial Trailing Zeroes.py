class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        def factorial(n):
            if n == 1:
                return 1
            else:
                return n*factorial(n-1)
        res = str(factorial(n))
        c = 0
        for i in res[::-1]:
            if int(i) > 0:
                break
            c += 1
        return c
