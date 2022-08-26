def missingnumber(nums):
    # n = len(nums)
    # if max(nums) == n-1:
    #     return n
    # else:
    #     for i in range(0, n+1):
    #         if i not in nums:
    #             return i

    n = len(nums)
    return int(((n*(n+1))/2) - sum(nums))


nums = [3, 0, 1]
print(missingnumber(nums))
