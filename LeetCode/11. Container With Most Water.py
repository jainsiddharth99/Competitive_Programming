def maxArea(height):
    n = len(height)
    res = 0
    l = 0
    r = n-1
    while l < r:
        area = min(height[l], height[r])*(r-l)
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return res
    # area=[]
    # for i in range(len(height)):
    #     for j in range(i+1,len(height)):
    #         k=min(height[i],height[j])*(j-i)
    #         area.append(k)
    # return max(area)


height = [1, 2, 1]
print(maxArea(height))
