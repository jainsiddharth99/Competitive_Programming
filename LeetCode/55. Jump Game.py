def canjump(nums):
    # edge case
    # target=len(nums) - 1
    # for i in range(len(nums)-1,-1,-1):
    #     if i+nums[target] >=target:
    #         target=i
    # return target==0

    j = 0
    for i, num in enumerate(nums):
        if i > j:
            return False
        j = max(j, num+i)

    return True


nums = [0]
print(canjump(nums))
