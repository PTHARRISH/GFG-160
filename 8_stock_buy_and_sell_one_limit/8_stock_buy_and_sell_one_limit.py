# Stock buy and sell with One Limit
# Best Approach
def maximumProfit(prices):
    res = 0
    min_value = prices[0]
    for i in range(len(prices)):
        min_value = min(prices[i], min_value)
        res = max(res, (prices[i] - min_value))
    return res


# time complexity: O(n)
# Space Complexity: O(1)


def maximumProfit(prices):
    res = 0
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            res = max(res, prices[j] - prices[i])
    return res


prices = list(map(int, input("enter the list:").split(",")))
print(maximumProfit(prices))  # 7, 10, 1, 3, 6, 9, 2
