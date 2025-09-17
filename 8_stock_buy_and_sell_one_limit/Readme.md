# Stock Buy and Sell with One Transaction

This document explains two approaches to solve the **Stock Buy and Sell (One Transaction Limit)** problem in Python. The goal is to find the maximum profit you can achieve by buying and selling a stock once.

---

## Approach 1: Single Pass (Best Approach)

### Debugger Walkthrough

- **Step 1:** Initialize `res` (result/profit) as 0 and `min_value` as the first price.
- **Step 2:** For each price in the list:
    - The debugger updates `min_value` to the minimum of the current price and `min_value` so far.
    - It calculates the profit if selling at the current price (`prices[i] - min_value`).
    - Updates `res` if this profit is greater than the previous `res`.
    - The debugger prints `min_value`, current price, and `res` at each step.
- **Step 3:** After the loop, returns `res` as the maximum profit.

---

## Approach 2: Brute Force (Two Loops)

### Debugger Walkthrough

- **Step 1:** Initialize `res` as 0.
- **Step 2:** For each pair of days `(i, j)` where `j > i`:
    - The debugger calculates the profit as `prices[j] - prices[i]`.
    - Updates `res` if this profit is greater than the previous `res`.
    - The debugger prints the pair `(i, j)`, their prices, and the current `res`.
- **Step 3:** After all pairs are checked, returns `res` as the maximum profit.

---

## What You Learned

- **Single Pass Optimization:** The debugger shows how tracking the minimum price so far allows for O(n) time.
- **Brute Force:** The debugger demonstrates checking all possible pairs, leading to O(n²) time.
- **Time Complexity:** The debugger confirms the first approach is linear, the second is quadratic.
- **Space Complexity:** Both approaches use constant space.

---

## Summary Table

| Approach     | Time Complexity | Space Complexity | Key Idea                |
| ------------ | -------------- | ---------------- | ----------------------- |
| Single Pass  | O(n)           | O(1)             | Track min price so far  |
| Brute Force  | O(n²)          | O(1)             | Check all pairs         |

---

## Real World Applications

- **Stock Trading:** Find the best day to buy and sell for maximum profit.
- **Commodity Pricing:** Optimize buy/sell timing for goods or currencies.
- **Real Estate:** Identify the best period to buy and sell property for profit.
- **Retail:** Analyze historical prices to maximize profit on inventory sales.
- **Cryptocurrency:** Determine the most profitable buy/sell points in volatile markets.

---

## How to Use

- Run either function with your list of prices.
- The debugger will show variable updates at each step.
- Both return the maximum profit possible with one buy and one sell.
- The single pass approach is more efficient for large datasets.
