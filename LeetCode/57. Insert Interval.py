def insert(intervals, newInterval):
    intervals.append(newInterval)
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

    # s, e = newInterval
    # res = []
    # for i in range(len(intervals)):
    #     if intervals[i][1] < newInterval.start:
    #         res.append(i)
    #     elif intervals[i][0] > newInterval.end:
    #         res.append(newInterval)
    #         return res+intervals[i:]
    #     else:
    #         newInterval.start = min(newInterval.start, intervals[i][0])
    #         newInterval.end = max(newInterval.end, intervals[i][1])
    # res.append([s, e])
    # return res


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(insert(intervals, newInterval))

"""
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""
