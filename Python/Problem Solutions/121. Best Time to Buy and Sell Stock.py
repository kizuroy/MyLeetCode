import timeit

def max_profit(prices):
    minPrice = float('inf')
    maxProfit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice

    return maxProfit

prices = [7,1,5,3,6,4]
print(max_profit(prices))

print(timeit.timeit(lambda: max_profit(prices), number=100000))
