class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = []
        for i, n in enumerate(prices):
            while s and prices[s[-1]] >= n:
                prices[s.pop()] -= n
            s.append(i)
        return prices
