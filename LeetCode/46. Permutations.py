def permute(nums):
    n = len(nums)
    # * edge cases
    if n == 0:
        return []
    if n == 1:
        return [nums]
    res = []
    # * main logic
    for i in range(n):
        fixed = nums[i]
        restlist = nums[:i]+nums[i+1:]
        for i in permute(restlist):
            curr = [fixed]+i
            if curr not in res:
                res.append(curr)
    return res


nums = [1, 2, 1]
a = permute(nums)
print(a)
