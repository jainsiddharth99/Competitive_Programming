from collections import defaultdict

# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
#         if len(points) == 1:
#             return 1

#         lines = defaultdict(lambda: set())
#         for i in range(len(points)):
#             for j in range(i+1, len(points)):
#                 x0, y0 = points[i]
#                 x1, y1 = points[j]
#                 line = find_line(x0, y0, x1, y1)
#                 lines[line].add(i)
#                 lines[line].add(j)
#         return max([len(lines[line])for line in lines])


# def find_line(x0, y0, x1, y1):
#     if y0 == y1:
#         return 0, y0
#     elif x0 == x1:
#         return x0, None
#     else:
#         slope = (y1-y0)/(x1-x0)
#         intercept = y0 - slope*x0
#         return slope, intercept


def maxPoints(points: list[list[int]]) -> int:
    # edge cases
    if len(points) == 1:
        return 1
    ans = 1
    for i, p1 in enumerate(points):
        slopes = defaultdict(int)
        for j, p2 in enumerate(points[i+1:]):
            slope = find_slope(p1, p2)
            slopes[slope] += 1
            ans = max(ans, slopes[slope])
    return ans+1


def find_slope(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1-x2 == 0:
        return float("inf")
    return (y1-y2)/(x1-x2)


points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print(maxPoints(points))
"""
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
"""
