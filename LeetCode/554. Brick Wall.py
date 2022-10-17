from collections import defaultdict


def leastBricks(wall: list[list[int]]) -> int:
    dt = defaultdict(int)
    for brick in wall:
        i = 0
        for j in range(len(brick)-1):
            i += brick[j]
            dt[i] += 1
    cnt = dt.values()
    return len(wall)-(max(cnt) if cnt else 0)


wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
print(leastBricks(wall))
