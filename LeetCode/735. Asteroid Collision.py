def asteroidCollision(asteroids: list[int]) -> list[int]:
    s = []
    for i in asteroids:
        while s and i < 0 < s[-1]:
            if s[-1] < -i:
                s.pop()
                continue
            elif s[-1] == -i:
                s.pop()
            break
        else:
            s.append(i)
    return s


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                s.append(asteroids[i])
            elif s and -(s[-1]) == asteroids[i]:
                s.pop()
            elif s and s[-1] > abs(asteroids[i]):
                continue
            elif s and s[-1] < abs(asteroids[i]):
                s.pop()
                s.append(asteroids[i])
        for i in s:
            if i < 0:
                return self.asteroidCollision(s)
        return s


asteroids = [-2, -1, 1, 2]
print(asteroidCollision(asteroids))

"""
Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 """
