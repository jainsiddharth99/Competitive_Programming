def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    i = j = n-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1

    if i == 0:
        nums.reverse()
        return

    while nums[i-1] >= nums[j]:
        j -= 1

    nums[j], nums[i-1] = nums[i-1], nums[j]

    nums[i:] = nums[n-1:i-1:-1]

    print(nums)


nums = [1, 3, 2]
nextPermutation(nums)
