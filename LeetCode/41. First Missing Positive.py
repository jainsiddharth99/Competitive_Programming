def firstMissingPositive(nums):

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


def firstMissingPositive2(nums: list[int]) -> int:
    for i, num in enumerate(nums):
        if num <= 0:
            nums[i] = 0

    for i, num in enumerate(nums):
        index = abs(num)-1
        if index >= 0 and index < len(nums):
            if nums[index] == 0:
                nums[index] = -inf
            elif nums[index] > 0:
                nums[index] *= -1

    for index, num in enumerate(nums):
        if num >= 0:
            return index + 1

    return len(nums) + 1


def firstMissingPositive3(nums):

    n = len(nums)
    i = 0
    while i < n:
        curr = nums[i]
        if 1 <= curr <= n:
            position = curr-1
            if nums[position] != curr:
                nums[i], nums[position] = nums[position], nums[i]
                i -= 1
        i += 1
    for i in range(n):
        if nums[i] != i+1:
            return i+1
    return n+1


nums = [3, 4, -1, 1]
print(firstMissingPositive3(nums))
