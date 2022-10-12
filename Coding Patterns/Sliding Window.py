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


def DynamicSlidingWindow(nums, total):
    minn = float('inf')
    s = 0
    e = 0
    curr = 0
    while e < len(nums):
        curr += nums[e]
        e += 1
        while s < e and curr >= total:
            curr -= nums[s]
            s += 1
            minn = min(minn, e-s+1)
    return minn


nums = [1, 2, 3, 4, 5, 9, 12, 22, 11]
print(DynamicSlidingWindow(nums, 30))
