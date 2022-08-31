def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    red = 0
    white = 0
    blue = n-1

    while white <= blue:
        if nums[white] == 0:
            nums[white], nums[red] = nums[red], nums[white]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1

    print(nums)


nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)


"""
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""
