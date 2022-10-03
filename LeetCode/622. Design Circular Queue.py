from collections import deque


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = deque()
        self.c = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.c < self.k:
            self.q.appendleft(value)
            self.c += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.q:
            return False
        else:
            self.q.pop()
            self.c -= 1
            return True

    def Front(self) -> int:
        if self.q:
            return self.q[-1]
        else:
            return -1

    def Rear(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return self.c == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
