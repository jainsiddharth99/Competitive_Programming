def merge(intervals: list[list[int]]) -> list[list[int]]:
    # intervals.sort(key=lambda x: x[0])

    intervals.sort(key=lambda x: x[0])
    # edge cases
    n = len(intervals)
    if n == 1:
        return intervals
    res = []

    for i in intervals:

        if not res or i[0] > res[-1][1]:
            res.append(i)
        else:
            res[-1][1] = max(res[-1][1], i[1])

    return res


intervals = [[1, 4], [4, 5]]
print(merge(intervals))
"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""
