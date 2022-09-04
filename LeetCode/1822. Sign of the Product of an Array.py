def arraySign(nums: list[int]) -> int:
    neg = 0
    pos = 0
    for i in nums:
        if i == 0:
            return 0
        elif i < 0:
            neg += 1

    if neg % 2 == 1:
        return -1
    else:
        return 1
