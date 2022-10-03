from collections import deque


class MyCircularDeque:

    def __init__(self, k: int):
        self.q = deque()
        self.k = k
        self.c = 0

    def insertFront(self, value: int) -> bool:
        if self.c < self.k:
            self.q.appendleft(value)
            self.c += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.c < self.k:
            self.q.append(value)
            self.c += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.q:
            return False
        else:
            self.q.popleft()
            self.c -= 1
            return True

    def deleteLast(self) -> bool:
        if not self.q:
            return False
        else:
            self.q.pop()
            self.c -= 1
            return True

    def getFront(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.q:
            return self.q[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return self.c == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
