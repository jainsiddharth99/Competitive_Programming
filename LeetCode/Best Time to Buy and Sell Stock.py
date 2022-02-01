prices = [7,5,3,6,4,1]

buy=min(prices)
l=[]
def stock():
    for i in range(len(prices)):
        if buy==prices[-1]:
            return 0
        elif prices[i]==buy:
            sell=max(prices[i+1:])
            return (sell-buy)
print(stock())