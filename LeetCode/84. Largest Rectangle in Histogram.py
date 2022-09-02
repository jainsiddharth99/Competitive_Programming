def nextsmaller(heights, n):
    stack = [-1]


def prevsmaller(heights, n):
    stack = [-1]
    prev = []
    for i in range(n-1, -1, -1):
        if stack[-1] > heights[i]:
            prev.append()
        else:
        stack.append(heights[i])
        prev.append()


def largestRectangleArea(heights: list[int]) -> int:
    # * brute force O(n^2)

    # n = len(heights)
    # area = 0
    # for i in range(n):
    #     for j in range(i, n):
    #         area = max(area, ((j-i) + 1) * min(heights[i:j+1]))
    # return area

    # efficient approach using stack
    # left smaller and right smaller

    n = len(heights)
    next = nextsmaller(heights, n)
    prev = prevsmaller(heights, n)

    for i in range(n):
        h =
        if next[i] == -1:
            next[i] = n
        w = next[i]-prev[i] - 1
        area = h*w
        max_area = max(area, max_area)
    return max_area


heights = [4, 2, 0, 3, 2, 4, 3, 4]
print(largestRectangleArea(heights))


"""
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""
