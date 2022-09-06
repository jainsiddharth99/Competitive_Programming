from collections import defaultdict


def majorityElement(nums: list[int]) -> int:
    dt = defaultdict(int)
    for i in nums:
        dt[i] += 1

    return max(dt, key=lambda x: dt[x])


nums = [3, 2, 3]
print(majorityElement(nums))
