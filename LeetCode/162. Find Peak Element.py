# O(n)
def findPeakElement(nums: list[int]) -> int:
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i
    return len(nums)-1
