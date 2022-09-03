
def nearestValidPoint(x: int, y: int, points: list[list[int]]) -> int:
    ans = -1
    md = float("inf")
    for i in range(len(points)):
        if points[i][0] == x or points[i][1] == y:
            man = abs(points[i][0]-x)+abs(points[i][1]-y)
            if man < md:
                ans = i
                md = man
    return ans


x = 3
y = 4
points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
print(nearestValidPoint(x, y, points))
