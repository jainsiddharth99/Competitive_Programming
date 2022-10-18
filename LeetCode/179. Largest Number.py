from functools import cmp_to_key


def largestNumber(nums: list[int]) -> str:
    for i, n in enumerate(nums):
        nums[i] = str(n)

    def compare(n1, n2):
        if n1+n2 > n2+n1:
            return -1
        else:
            return 1

    nums = sorted(nums, key=cmp_to_key(compare))

    return str(int("".join(nums)))


nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))
