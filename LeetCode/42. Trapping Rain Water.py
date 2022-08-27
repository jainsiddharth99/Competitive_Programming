def trap(height: list[int]) -> int:
    """
    Method 1:
    as volume depends on the heights of bars, and since only
    we will move from left or right dependinf on the situation,
    Like if we have [3,1,0,1,2]
    here we can consider lmax=3 and rmax=2
    since there is no num in list is >=3 we have to use
    rmax and calculate volume according to that
    """
    # res = 0
    # n = len(height)
    # l, r = 0, n-1
    # l_max, r_max = height[l], height[r]
    # while l < r:
    #     l_max, r_max = max(l_max, height[l]), max(r_max, height[r])
    #     if l_max <= r_max:
    #         res += l_max-height[l]
    #         l += 1
    #     else:
    #         res += r_max-height[r]
    #         r -= 1
    # return res

    """
    Method 2:
    we create two list which iterate left and another from end
    we add result according height filled(we select minimum)
    """
    level = []
    left, right = 0, 0
    for i in height:
        left = max(left, i)
        level += [left]
    for j, h in reversed(list(enumerate(height))):
        right = max(right, h)
        level[j] = (min(right, level[j]))-h
    return sum(level)

    """
    Method 3: 
    same as before just more clear
    
    """

    # n = len(height)
    # res = 0
    # l_max = []
    # r_max = []
    # i, j = 1, 1
    # l_max.append(height[0])
    # while i < n:
    #     l_max.append(max(height[i], l_max[i-1]))
    #     i += 1
    # height.reverse()
    # r_max.append(height[0])
    # while j < n:
    #     r_max.append(max(height[j], r_max[j-1]))
    #     j += 1
    # height.reverse()
    # r_max.reverse()
    # for i in range(n):
    #     res += ((min(r_max[i], l_max[i])) - height[i])
    # return res
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
