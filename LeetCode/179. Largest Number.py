import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            xy = int(str(x)+str(y))
            yx = int(str(y)+str(x))
            return yx-xy

        nums.sort(key=functools.cmp_to_key(compare))
        return "".join([str(i) for i in nums])
