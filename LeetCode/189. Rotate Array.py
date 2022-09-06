def rotate(nums, k):

    nums[:] = nums[-(k % len(nums)):]+nums[:-(k % len(nums))]


nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)
