class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n == 4:
                return False
        return True
