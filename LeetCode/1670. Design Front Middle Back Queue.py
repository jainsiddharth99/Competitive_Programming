
class FrontMiddleBackQueue:

    def __init__(self):
        self.q = []

    def pushFront(self, val: int) -> None:
        self.q.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.q.insert(len(self.q)//2, val)

    def pushBack(self, val: int) -> None:

        self.q.append(val)

    def popFront(self) -> int:

        return self.q.pop(0) if self.q else -1

    def popMiddle(self) -> int:
        if len(self.q) < 3:
            return self.q.pop(0) if self.q else -1
        return self.q.pop(((len(self.q)-1)//2)) if self.q else -1

    def popBack(self) -> int:
        return self.q.pop() if self.q else -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
