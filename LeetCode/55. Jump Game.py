def canjump(nums):
    # edge case
    # target=len(nums) - 1
    # for i in range(len(nums)-1,-1,-1):
    #     if i+nums[target] >=target:
    #         target=i
    # return target==0

    n = len(nums)
    target_index = n-1
    curr_max_index = 0
    for i in range(n):
        if i > curr_max_index:
            return False
        curr_max_index = max(i+nums[i], curr_max_index)
    return True


nums = [0]
print(canjump(nums))
