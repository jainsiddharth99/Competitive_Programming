def findPoisonedDuration(timeSeries: list[int], duration: int) -> int:
    n = len(timeSeries)
    if n == 0:
        return 0
    total = 0
    for i in range(n-1):
        total += min(timeSeries[i+1]-timeSeries[i], duration)

    return total+duration


timeSeries = [1, 2]
duration = 2
print(findPoisonedDuration(timeSeries, duration))

"""
Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
"""
