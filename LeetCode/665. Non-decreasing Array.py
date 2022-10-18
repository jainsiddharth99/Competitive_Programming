def checkPossibility(nums: list[int]) -> bool:
    done = False
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            continue
        if done:
            return False

        if i == 0 or nums[i+1] >= nums[i-1]:
            nums[i] = nums[i+1]
        else:
            nums[i+1] = nums[i]
        done = True
    return True


nums = [4, 3, 2, 1]
print(checkPossibility(nums))
