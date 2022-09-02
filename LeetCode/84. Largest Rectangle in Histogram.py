# def nextsmaller(heights, n):
#     stack = [-1]
#     next = [-1]*n
#     for i in range(n-1, -1, -1):
#         curr = heights[i]
#         while stack[-1] != -1 and heights[stack[-1]] > curr:
#             stack.pop()

#         next[i] = stack[-1]
#         stack.append(i)
#     return next


# def prevsmaller(heights, n):
#     stack = [-1]
#     prev = [-1]*n
#     for i in range(n):
#         curr = heights[i]
#         while stack[-1] != -1 and heights[stack[-1]] >= curr:
#             stack.pop()

#         prev[i] = stack[-1]
#         stack.append(i)
#     return prev


# def largestRectangleArea(heights: list[int]) -> int:

#     n = len(heights)
#     next = nextsmaller(heights, n)
#     prev = prevsmaller(heights, n)
#     max_area = 0
#     for i in range(n):
#         h = heights[i]
#         if next[i] == -1:
#             next[i] = n
#         w = next[i]-prev[i] - 1
#         area = h*w
#         max_area = max(area, max_area)
#     return max_area

def largestRectangleArea(heights: list[int]) -> int:
    n = len(heights)
    maxArea = 0
    stack = []
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height*(i-index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h*(n-i))
    return maxArea


heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))


"""
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""
# * brute force O(n^2)

# n = len(heights)
# area = 0
# for i in range(n):
#     for j in range(i, n):
#         area = max(area, ((j-i) + 1) * min(heights[i:j+1]))
# return area

# efficient approach using stack
# left smaller and right smaller
