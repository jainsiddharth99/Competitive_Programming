prices = [7,5,3,6,4,1]
buy=min(prices)
def stock():
    for i in range(len(prices)):
        if buy==prices[-1]:
            return 0
        elif prices[i]==buy:
            sell=max(prices[i+1:])
            return (sell-buy)
print(stock())

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         maxProfit = 0
#         minPurchase = prices[0]
#         for i in range(1, len(prices)):		
#             maxProfit = max(maxProfit, prices[i] - minPurchase)
#             minPurchase = min(minPurchase, prices[i])
#         return maxProfit