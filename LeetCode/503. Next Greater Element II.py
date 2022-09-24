def nextGreaterElements1(nums: list[int]) -> list[int]:
    n = len(nums)*2
    res = [-1]*n
    s = []
    nums += nums
    for i in range(n-1, -1, -1):
        while s and s[-1] <= nums[i]:
            s.pop()
        res[i] = s[-1] if s else -1
        s.append(nums[i])
    return res[:n//2]


def nextGreaterElements2(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [-1]*n
    s = []
    nums += nums
    for i in range(2*(n-1), -1, -1):
        while s and s[-1] <= nums[i % n]:
            s.pop()
        res[i % n] = s[-1] if s else -1
        s.append(nums[i % n])
    return res


nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
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
