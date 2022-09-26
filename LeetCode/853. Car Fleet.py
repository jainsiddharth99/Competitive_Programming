from collections import defaultdict


def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    n = len(position)
    s = []
    for i in range(n-1, -1, -1):
        s.append([position[i], speed[i]])

    s.sort(key=lambda x: (x[0], x[1]), reverse=True)

    st = []
    for p, s in s:
        dist = target-p
        if not st:
            st.append(dist/s)
        elif dist/s > st[-1]:
            st.append(dist/s)
    return len(st)


target = 10
position = [6, 8]
speed = [3, 2]
print(carFleet(target, position, speed))
"""

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
Example 2:

Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.
Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
 """
