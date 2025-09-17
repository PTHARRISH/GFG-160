# Maximum Subarray Sum

This document explains two approaches to solve the **Maximum Subarray Sum** problem in Python. The goal is to find the largest sum of a contiguous subarray within a one-dimensional array of numbers.

---

## Approach 1: Kadane's Algorithm (Optimal, Single Pass)

### Debugger Walkthrough

- **Step 1:** Initialize `res` and `max_end` to the first element of the array.
- **Step 2:** For each element from the second to the last:
    - Update `max_end` to be the maximum of the current element or `max_end + current element`.
    - Update `res` if `max_end` is greater than the current `res`.
    - The debugger prints `max_end` and `res` at each step.
- **Step 3:** After the loop, return `res` as the maximum subarray sum.

---

## Approach 2: Iterative (Brute Force, Nested Loops)

### Debugger Walkthrough

- **Step 1:** Initialize `res` to the first element.
- **Step 2:** For each starting index `i`:
    - Set `curr_sum` to 0.
    - For each ending index `j` from `i` to the end:
        - Add `arr[j]` to `curr_sum`.
        - Update `res` if `curr_sum` is greater.
        - The debugger prints `curr_sum` and `res` at each step.
- **Step 3:** After all loops, return `res`.

---

## What You Learned

- **Kadane’s Algorithm:** Efficiently tracks the running maximum subarray sum in a single pass.
- **Brute Force:** Checks all possible subarrays using nested loops.
- **Time Complexity:** Kadane’s is O(n); brute force is O(n²).
- **Space Complexity:** Both use O(1) extra space.
- **Optimality:** Kadane’s is the best possible for this problem.

---

## Summary Table

| Approach      | Time Complexity | Space Complexity | Key Idea         |
| ------------- | --------------- | ---------------- | ---------------- |
| Kadane's      | O(n)            | O(1)             | Running max sum  |
| Brute Force   | O(n²)           | O(1)             | All subarrays    |

---

## Real World Applications

- **Gaming/Scoring Systems:** Find the best scoring streak in a game.
- **GitHub Contribution Streak Tracker:** Identify the longest streak of daily contributions.
- **Financial Analysis:** Detect the most profitable period in stock prices.
- **Sensor Data:** Find periods of maximum activity in time-series data.
- **Weather Analysis:** Locate the warmest or coldest consecutive days.

---

## How to Use

- Run either function with your array.
- The debugger will show variable updates at each step.
- Both return the maximum subarray sum.
- Kadane’s algorithm is recommended for efficiency.
