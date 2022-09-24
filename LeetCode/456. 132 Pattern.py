def find132pattern1(nums: list[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False
    mid = float("-inf")
    s = []
    for i in range(n-1, -1, -1):
        if nums[i] < mid:
            return True

        while s and s[-1] < nums[i]:
            mid = s.pop()
        s.append(nums[i])

    return False


def find132pattern2(nums: list[int]) -> bool:
    stack = []
    minstack = []
    currmin = nums[0]
    for i in nums[1:]:
        while stack and i > stack[-1]:
            stack.pop()
            minstack.pop()
        if stack and i > minstack[-1]:
            return True
        stack.append(i)
        minstack.append(currmin)
        currmin = min(currmin, i)
    return False


nums = [3, 1, 4, 2]
print(find132pattern2(nums))

"""

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

"""
