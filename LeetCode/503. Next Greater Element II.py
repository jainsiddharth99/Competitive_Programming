def nextGreaterElements(nums: list[int]) -> list[int]:
    pass


nums = [1, 2, 3, 4, 3]
print(nextGreaterElements(nums))

"""
Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
"""
