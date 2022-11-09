import bisect


class MedianFinder:

    def __init__(self):
        self.lt = []

    def addNum(self, num: int) -> None:
        if self.lt:
            if self.lt[-1] < num:
                self.lt.append(num)
            else:
                bisect.insort(self.lt, num)
        else:
            self.lt.append(num)

    def findMedian(self) -> float:

        n = len(self.lt)
        print(n)
        if n % 2 == 1:
            return self.lt[n//2]
        else:

            val = self.lt[n//2]+self.lt[(n//2)-1]
            val /= 2
            return val


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
