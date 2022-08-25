def findDisappearedNumbers(nums):
    n = len(nums)
    for i in range(n):
        temp = abs(nums[i])-1
        if nums[temp] > 0:
            nums[temp] *= -1

    res = []
    for i in range(n):
        if nums[i] > 0:
            res.append(i+1)
    return res


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))
