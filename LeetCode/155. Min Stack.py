from collections import deque


class MinStack:

    def __init__(self):
        self.st = deque()

    def push(self, val: int) -> None:
        return self.st.append(val)

    def pop(self) -> None:
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return min(self.st)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
