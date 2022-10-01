def getCollisionTimes(cars: list[list[int]]) -> list[float]:
    n = len(cars)
    ans = [-1]*n
    s = []
    for i in range(n-1, -1, -1):


cars = [[1, 2], [2, 1], [4, 3], [7, 2]]
print(getCollisionTimes(cars))

"""
 

Example 1:

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
Example 2:

Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]
 
"""
