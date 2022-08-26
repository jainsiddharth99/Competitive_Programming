def findDisappearedNumbers(nums):
    # * first approach
    # n = len(nums)
    # for i in range(n):
    #     temp = abs(nums[i])-1
    #     if nums[temp] > 0:
    #         nums[temp] *= -1

    # res = []
    # for i in range(n):
    #     if nums[i] > 0:
    #         res.append(i+1)
    # return res

    n = len(nums)
    s = set(nums)
    res = []
    for i in range(1, n+1):
        if i not in s:
            res.append(i)
    return res


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))
