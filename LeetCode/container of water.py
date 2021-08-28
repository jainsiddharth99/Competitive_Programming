def maxArea(height):
    area=[]
    for i in range(len(height)):
        for j in range(i+1,len(height)):
            k=min(height[i],height[j])*(j-i)
            area.append(k)
    return max(area)

height=[1,8,6,2,5,4,8,3,7]
print(maxArea(height))
