import numpy as np


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = [int(a) for a in str(n)]
        return (np.prod(x) - sum(x))
