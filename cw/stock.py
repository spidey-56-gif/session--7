# Time Complexity: O(n)
# Space Complexity: O(1)

def maxProfit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
                
    return max_profit

# Test Executions
print("Test A:", maxProfit([7, 1, 5, 3, 6, 4]))
print("Test B:", maxProfit([7, 6, 4, 3, 1]))
print("Test C:", maxProfit([2, 4, 1]))
