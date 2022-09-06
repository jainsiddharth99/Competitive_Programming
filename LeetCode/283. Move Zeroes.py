def moveZeroes(nums: list[int]):
    """
    Do not return anything, modify nums in-place instead.
    """
    count = 0
    for i in nums:
        if i == 0:
            count += 1
    for i in range(count):
        nums.remove(0)
        nums.append(0)
    print(nums)


nums = [0, 0, 1]
moveZeroes(nums)
