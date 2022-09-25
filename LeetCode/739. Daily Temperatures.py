def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    res = [0]*n
    s = []
    curr = n-1
    for i in range(n-1, -1, -1):
        while s and s[-1][0] <= temperatures[i]:
            s.pop()
        if s:
            curr = s[-1][1]
        res[i] = curr-i
        s.append([temperatures[i], i])

    return res


def dailyTemperatures2(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    res = [0]*n
    s = []
    for i, v in enumerate(temperatures):
        while s and s[-1][1] < v:
            ind, val = s.pop()
            res[ind] = i-ind
        s.append([i, v])
    return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures2(temperatures))


""" 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 """
