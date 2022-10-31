from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lt = [str(i) for i in range(1, n+1)]
        perm = permutations("".join(lt))
        c = 0
        for i in perm:
            if c == k-1:
                return "".join(i)
            else:
                c += 1
                continue
