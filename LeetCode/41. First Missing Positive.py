def firstMissingPositive(nums):
    # * edge cases
    if 1 not in nums:
        return 1
    high = max(nums)
    low = min(nums)

    if high < 1:
        return 1
    if low > 1:
        return 1
    if high == 1:
        return 2

    # * main logic

    n = len(nums)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n+1
    for i in range(n):
        temp = abs(nums[i]) - 1
        if temp < n and nums[temp] > 0:
            nums[temp] *= -1

    for i in range(n):
        if nums[i] > 0:
            return i+1

    else:
        return n+1


nums = [1, 2, 0]
print(firstMissingPositive(nums))
