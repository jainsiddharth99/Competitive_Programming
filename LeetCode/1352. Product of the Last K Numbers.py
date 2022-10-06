
class ProductOfNumbers:

    def __init__(self):
        self.lt = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.lt = [1]
        else:
            self.lt.append(self.lt[-1]*num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.lt):
            return 0
        return self.lt[-1]//self.lt[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
