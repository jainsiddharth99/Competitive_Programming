def canjump(nums):
    # edge case
    j = 0
    for i, num in enumerate(nums):
        if i > j:
            return False
        j = max(j, num+i)

    return True


nums = [0, 1]
print(canjump(nums))
