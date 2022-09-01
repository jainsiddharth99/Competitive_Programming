def singleNumber(nums: list[int]) -> int:
    return sum(list(set(nums)))*2 - sum(nums)
