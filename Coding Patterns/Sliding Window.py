def SlidingWindow(nums, k):
    maxx = float('-inf')
    curr = sum(nums[:k])
    s = 0
    e = k
    while e < len(nums):
        maxx = max(curr, maxx)
        curr += nums[e]
        curr -= nums[s]
        s += 1
        e += 1
    return max(curr, maxx)


nums = [1, 6, 8, 13, 5, 6, 34, 6, 8, 45, 45]
k = 2
print(SlidingWindow(nums, k))


def DynamicSlidingWindow(nums):
    maxx = float('-inf')
    return maxx
