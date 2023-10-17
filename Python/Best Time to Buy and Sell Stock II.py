def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

prices = [1,2,3,4,5]
print(max_profit(prices))

'''
This Python function, `max_profit`, calculates the maximum profit that can be made from a given list of stock prices. 
It does this by adding up all the positive differences between consecutive days. 
The function assumes that multiple transactions are allowed, but selling must occur before a new purchase. The time complexity is O(n), and it uses constant space.
'''