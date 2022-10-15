# TLE - Brute Force
def findPairs1(nums: list[int], k: int) -> int:
    res = set()
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j]-nums[i] == k:
                res.add((nums[i], nums[j]))
            if nums[i]-nums[j] == k:
                res.add((nums[j], nums[i]))
    return len(res)

# working


def findPairs2(nums: list[int], k: int) -> int:
    res = set()
    i = 0
    j = 1
    nums.sort()
    while j < len(nums):
        if nums[j]-nums[i] == k:
            res.add((nums[i], nums[j]))
            i += 1
            j = i+1
        else:
            j += 1

    return len(res)


nums = [3, 1, 4, 1, 5]
k = 2
print(findPairs2(nums, k))
