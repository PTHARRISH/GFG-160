# 7 - Stock Buy and Sell (With No Limit)

This document explains two approaches to solve the **Stock Buy and Sell (With No Limit)** problem in Python. The goal is to maximize profit by buying and selling stocks as many times as you like (but you must sell before you buy again).

---

## Approach 1: Greedy (Best Approach)

### Debugger Walkthrough

- **Step 1:** Initialize `res` (result/profit) to 0.
- **Step 2:** Loop through the price array from index 0 to n-2.
    - The debugger checks if the next day's price is higher than the current day's.
    - If so, it adds the difference to `res` (simulating a buy today and sell tomorrow).
    - The debugger prints the current profit after each transaction.
- **Step 3:** After the loop, the debugger returns the total profit.

**Code Example:**
```python
def maximumProfit(prices):
        n = len(prices)
        res = 0
        for i in range(0, n - 1):
                if prices[i] < prices[i + 1]:
                        res += prices[i + 1] - prices[i]
        return res
```

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Approach 2: Valley-Peak (Alternative)

### Debugger Walkthrough

- **Step 1:** Initialize `res` to 0, `lmin` and `lmax` to the first price, and index `i` to 0.
- **Step 2:** While `i` is less than n-1:
    - The debugger finds the next valley (local minimum) by skipping days where the price is falling or flat.
    - Sets `lmin` to this valley.
    - Then, finds the next peak (local maximum) by skipping days where the price is rising or flat.
    - Sets `lmax` to this peak.
    - Adds `lmax - lmin` to `res`.
    - The debugger prints each buy/sell pair and the profit.
- **Step 3:** Returns the total profit.

**Code Example:**
```python
def maximumProfit(prices):
        n = len(prices)
        res = 0
        lmin = prices[0]
        lmax = prices[0]
        i = 0
        while i < n - 1:
                while i < n - 1 and prices[i] >= prices[i + 1]:
                        i += 1
                lmin = prices[i]
                while i < n - 1 and prices[i] <= prices[i + 1]:
                        i += 1
                lmax = prices[i]
                res += lmax - lmin
        return res
```

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## What You Learned

- **Greedy Approach:** The debugger shows how to accumulate profit on every upward price movement.
- **Valley-Peak Approach:** The debugger demonstrates finding local minima and maxima for each transaction.
- **Time Complexity:** Both approaches require only a single pass through the array.
- **Space Complexity:** Both use constant extra space.

---

## Summary Table

| Approach      | Time Complexity | Space Complexity | Key Idea                |
| ------------- | --------------- | ---------------- | ----------------------- |
| Greedy        | O(n)            | O(1)             | Add all upward moves    |
| Valley-Peak   | O(n)            | O(1)             | Buy at valleys, sell at peaks |

---

## Real World Applications

- **Stock Trading Bots:** Automate buying and selling for maximum profit in volatile markets.
- **Commodity Trading:** Optimize buy/sell decisions for goods with fluctuating prices.
- **Cryptocurrency Trading:** Maximize gains in highly dynamic crypto markets.
- **Retail Inventory:** Decide when to restock or sell based on price trends.
- **Energy Markets:** Buy and sell energy contracts for profit as prices change.

---

## How to Use

- Run either function with your price array.
- The debugger will show profit updates at each step.
- Both return the maximum achievable profit.
- The greedy approach is simpler and more direct.
