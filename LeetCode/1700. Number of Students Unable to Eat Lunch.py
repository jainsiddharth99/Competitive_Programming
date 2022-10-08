from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = 0
        n = len(students)
        while c != n:
            if sandwiches[0] == students[0]:
                c = 0
                sandwiches.pop(0)
                students.pop(0)
                n = len(students)
            else:
                students.append(students.pop(0))
                c += 1

        return len(students)
